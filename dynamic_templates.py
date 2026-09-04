# ============================================================
# PERSISTENT CHANNEL/TEMPLATE STORE
# One file per channel. Runtime code is never rewritten by the bot.
# ============================================================
import json
import os
import re
from pathlib import Path
from telethon.tl import types
from telethon.tl.types import MessageEntityCustomEmoji

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / 'data'
CHANNEL_DIR = DATA_DIR / 'channels'
LEGACY_FILE = ROOT / 'dynamic_channels.json'
MIRROR_FILE = ROOT / 'channel_configs.py'
CHANNEL_DIR.mkdir(parents=True, exist_ok=True)

TEMPLATE_STEPS = [
    ('toss', '🎯 TOSS', '{TEAM}, {LEAGUE}'),
    ('toss_promo', '📣 TOSS PROMO', '{TEAM}, {LEAGUE}'),
    ('toss_pass', '🎯 TOSS PASS', '{TEAM}, {CHOICE}'),
    ('match', '🏏 MATCH', '{TEAM1}, {TEAM2}, {WINNER}, {LEAGUE}'),
    ('match_promo1', '📣 MATCH PROMO 1', '{TEAM1}, {TEAM2}, {WINNER}, {LEAGUE}'),
    ('match_promo2', '📣 MATCH PROMO 2', '{TEAM1}, {TEAM2}, {WINNER}, {LEAGUE}'),
    ('match_pass', '🏆 MATCH PASS', '{TEAM}, {RESULT}'),
    ('session', '🔥 SESSION', '{OVER}, {RUN}, {CALL}, {CALL_EMOJI}'),
    ('session_pass', '🔥 SESSION PASS', '{OVER}, {RESULT}'),
    ('session_loss', '❌ SESSION LOSS', '(no variable needed)'),
    ('sball', '⚡ S-BALL', '{BALL}, {RUN}, {CALL}, {CALL_EMOJI}'),
    ('sball_pass', '⚡ S-BALL PASS', '{BALL}, {RESULT}'),
    ('sball_loss', '❌ S-BALL LOSS', '(no variable needed)'),
    ('entry', '📥 ENTRY', '{CALL}, {RATE}, {FAV}, {LIMIT}, {KHAO}, {WIN}'),
    ('break', '⏸️ BREAK', '{TARGET}, {PREDICTION}, {WINNER}'),
    ('cashout', '💰 CASHOUT', '{ENTRY}, {CALL}, {RATE}, {FAV}, {LIMIT}, {KHAO}, {WIN}'),
]


def _safe_name(name):
    return re.sub(r'[^A-Za-z0-9_.-]+', '_', str(name).strip().upper())[:80] or 'CHANNEL'


def _path(name):
    return CHANNEL_DIR / f'{_safe_name(name)}.json'


def _read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data if isinstance(data, dict) else None
    except Exception as exc:
        print(f'⚠️ Cannot read {path}: {exc}')
        return None


def _atomic_write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


def _migrate_legacy_json():
    if not LEGACY_FILE.exists():
        return
    legacy = _read_file(LEGACY_FILE)
    if not legacy or not isinstance(legacy.get('channels'), dict):
        return
    for name, data in legacy['channels'].items():
        p = _path(name)
        if not p.exists() and isinstance(data, dict):
            _atomic_write(p, {'name': name, 'id': data.get('id'), 'templates': data.get('templates', {})})


def list_dynamic_channels():
    _migrate_legacy_json()
    result = {}
    for p in sorted(CHANNEL_DIR.glob('*.json')):
        data = _read_file(p)
        if data and data.get('name'):
            result[str(data['name'])] = data
    return result


def get_channel_data(name):
    _migrate_legacy_json()
    return _read_file(_path(name))


def is_dynamic_channel(channel_name):
    return _path(channel_name).exists()


def add_dynamic_channel(name, channel_id):
    name = str(name).strip().upper()
    data = {'name': name, 'id': int(channel_id), 'templates': {}}
    _atomic_write(_path(name), data)
    generate_python_config()


def remove_dynamic_channel(name):
    p = _path(name)
    existed = p.exists()
    if existed:
        p.unlink()
    generate_python_config()
    return existed


def save_template(channel_name, kind, template_data):
    name = str(channel_name).strip().upper()
    data = get_channel_data(name) or {'name': name, 'id': None, 'templates': {}}
    data.setdefault('templates', {})[kind] = template_data
    _atomic_write(_path(name), data)
    generate_python_config()


def commit_channel(name, channel_id, templates):
    name = str(name).strip().upper()
    data = {'name': name, 'id': int(channel_id), 'templates': templates or {}}
    _atomic_write(_path(name), data)
    generate_python_config()


def save_template_data(message):
    entities = getattr(message, 'entities', None) or []
    custom_emojis = []
    for entity in entities:
        if isinstance(entity, MessageEntityCustomEmoji):
            custom_emojis.append({'offset': entity.offset, 'length': entity.length, 'document_id': entity.document_id})
    return {
        'text': message.raw_text or '',
        'entities': serialize_entities(entities),
        'custom_emojis': custom_emojis,
        'saved_at': __import__('datetime').datetime.now().isoformat(timespec='seconds'),
    }


def get_template(channel_name, kind):
    data = get_channel_data(channel_name)
    if not data:
        return None
    return (data.get('templates') or {}).get(kind)


def render_template(channel_name, kind, values):
    tpl = get_template(channel_name, kind)
    if not tpl:
        return None, []

    text = tpl.get('text', '') or ''
    values = values or {}

    # Accept {CALL}, { CALL }, {call}, { call }, etc.
    normalized = {
        str(k).strip().upper(): str(v)
        for k, v in values.items()
        if v is not None
    }

    token_re = re.compile(r'\{\s*([A-Za-z0-9_]+)\s*\}')

    matches = []
    for m in token_re.finditer(text):
        key = m.group(1).strip().upper()
        if key in normalized:
            matches.append((m.start(), m.end(), normalized[key]))

    if matches:
        out = []
        ranges = []
        cursor = 0
        for start, end, value in matches:
            out.append(text[cursor:start])
            out.append(value)
            ranges.append((
                utf16_index(text, start),
                utf16_index(text, end),
                utf16_length(value),
            ))
            cursor = end
        out.append(text[cursor:])
        rendered = ''.join(out)
    else:
        rendered = text
        ranges = []

    entities = deserialize_entities(tpl.get('entities', []))
    for entity in entities:
        old_start = entity.offset
        old_end = entity.offset + entity.length
        entity.offset = _map_offset(old_start, ranges)
        entity.length = max(
            0,
            _map_offset(old_end, ranges) - entity.offset
        )

    return rendered, entities

def serialize_entities(entities):
    result = []
    for entity in entities or []:
        try:
            attrs = {}
            # TLObjects expose fields through __slots__ / to_dict rather than vars().
            if hasattr(entity, 'to_dict'):
                raw = entity.to_dict()
                attrs = {k: v for k, v in raw.items() if k != '_' and isinstance(v, (str, int, bool)) or v is None}
                attrs.pop('_', None)
            else:
                for key in getattr(entity, '__slots__', ()):
                    value = getattr(entity, key, None)
                    if isinstance(value, (str, int, bool)) or value is None:
                        attrs[key] = value
            result.append({'type': entity.__class__.__name__, 'attrs': attrs})
        except Exception as exc:
            print('⚠️ entity serialization:', exc)
    return result


def deserialize_entities(items):
    result = []
    for item in items or []:
        try:
            cls = getattr(types, item['type'])
            result.append(cls(**item.get('attrs', {})))
        except Exception as exc:
            print('⚠️ entity deserialize:', exc)
    return result


def utf16_length(text):
    return len((text or '').encode('utf-16-le')) // 2


def utf16_index(text, position):
    return utf16_length((text or '')[:position])


def _replace_with_tracking(text, replacements):
    if not text:
        return text, []
    matches = []
    for token, value in replacements.items():
        for m in re.finditer(re.escape(token), text):
            matches.append((m.start(), m.end(), str(value)))
    matches.sort(key=lambda x: (x[0], x[1]))
    chosen, last_end = [], -1
    for item in matches:
        if item[0] < last_end:
            continue
        chosen.append(item); last_end = item[1]
    if not chosen:
        return text, []
    out, ranges, cursor = [], [], 0
    for start, end, value in chosen:
        out.extend((text[cursor:start], value))
        ranges.append((utf16_index(text, start), utf16_index(text, end), utf16_length(value)))
        cursor = end
    out.append(text[cursor:])
    return ''.join(out), ranges


def _map_offset(old_offset, ranges):
    delta = 0
    for start, end, new_len in ranges:
        old_len = end - start
        if old_offset >= end:
            delta += new_len - old_len
        elif old_offset > start:
            delta += new_len - (old_offset - start)
    return max(0, old_offset + delta)


def channel_id(name):
    data = get_channel_data(name)
    return data.get('id') if data else None


def template_help(kind):
    for key, label, vars_text in TEMPLATE_STEPS:
        if key == kind:
            return label, vars_text
    return kind.upper(), ''


def generate_python_config(data=None):
    # Human-readable mirror only. Runtime source of truth is data/channels/*.json.
    if data is None:
        data = {'channels': list_dynamic_channels()}
    channels = data.get('channels', data) if isinstance(data, dict) else {}
    lines = [
        '# AUTO-GENERATED MIRROR — runtime does NOT depend on this file.',
        '# Edit channels/templates through the Telegram control bot.',
        '',
        'CHANNEL_CONFIGS = ' + repr(channels),
        '',
    ]
    _atomic_write(MIRROR_FILE, {'_text': '\n'.join(lines)}) if False else MIRROR_FILE.write_text('\n'.join(lines), encoding='utf-8')
