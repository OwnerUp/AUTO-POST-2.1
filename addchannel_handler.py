# ============================================================
# AUTO POST CONTROL BOT
# Separate Telegram Bot = configuration/control only.
# User session = existing posting commands.
# ============================================================
import json
from pathlib import Path
from telethon import events, Button
from dynamic_templates import (
    TEMPLATE_STEPS, save_template_data, commit_channel, get_channel_data,
    list_dynamic_channels, remove_dynamic_channel, channel_id,
    generate_python_config,
)
from channels import CHANNELS


def register_addchannel_handler(bot, owner_id):
    state_file = Path(__file__).with_name('control_state.json')
    owner_key = str(int(owner_id))

    def load_state():
        try:
            return json.loads(state_file.read_text(encoding='utf-8')) if state_file.exists() else {}
        except Exception:
            return {}

    state = load_state()

    def refresh_state():
        nonlocal state
        state = load_state()
        return state

    def persist():
        tmp = state_file.with_suffix('.tmp')
        tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')
        tmp.replace(state_file)

    def allowed(event):
        return bool(event.is_private and event.sender_id == int(owner_id))

    def label(kind):
        return next((x[1] for x in TEMPLATE_STEPS if x[0] == kind), kind.upper())

    def vars_for(kind):
        return next((x[2] for x in TEMPLATE_STEPS if x[0] == kind), '')

    def all_channels():
        out = dict(CHANNELS)
        out.update({n: d.get('id') for n, d in list_dynamic_channels().items() if d.get('id') is not None})
        return out

    def channel_rows(prefix='tm_edit_channel'):
        rows, row = [], []
        for name in all_channels():
            row.append(Button.inline(f'📢 {name}', f'{prefix}:{name}'.encode()))
            if len(row) == 2:
                rows.append(row); row = []
        if row: rows.append(row)
        rows += [[Button.inline('➕ NEW CHANNEL', b'tm_new')], [Button.inline('🏠 MAIN MENU', b'tm_home')]]
        return rows

    def template_rows(channel_name=None):
        rows, row = [], []
        for kind, text, _ in TEMPLATE_STEPS:
            cb = f'tm_kind:{kind}:{channel_name}' if channel_name else f'tm_kind:{kind}'
            row.append(Button.inline(text, cb.encode()))
            if len(row) == 2:
                rows.append(row); row = []
        if row: rows.append(row)
        return rows

    def nav(back='tm_back', cancel='tm_cancel'):
        return [[Button.inline('⬅️ BACK', back.encode()), Button.inline('❌ CANCEL', cancel.encode())]]

    async def home(event):
        await event.respond(
            '🤖 AUTO POST — CONTROL PANEL\n\n'
            'यहाँ से तुम बिना code खोले channels और templates manage कर सकते हो.\n\n'
            '➡️ कोई button दबाओ; मैं अगला step खुद बताऊँगा.',
            buttons=[
                [Button.inline('➕ NEW CHANNEL', b'tm_new')],
                [Button.inline('✏️ EDIT CHANNEL', b'tm_edit_channels')],
                [Button.inline('📋 ALL CHANNELS', b'tm_all_channels')],
                [Button.inline('❓ HELP', b'tm_help')],
            ],
        )

    async def show_channels(event):
        await event.respond(
            f'📢 SELECT CHANNEL\n\nकुल channels: {len(all_channels())}\n\n'
            'जिस channel को edit करना है उस पर tap करो.',
            buttons=channel_rows(),
        )

    async def show_channel(event, s):
        name = s['channel']
        data = get_channel_data(name) or {}
        overridden = set((data.get('templates') or {}).keys())
        rows, row = [], []
        for kind, text, _ in TEMPLATE_STEPS:
            mark = '🟢' if kind in overridden else '⚪'
            row.append(Button.inline(f'{mark} {text}', f'tm_kind:{kind}:{name}'.encode()))
            if len(row) == 2:
                rows.append(row); row = []
        if row: rows.append(row)
        rows += [
            [Button.inline('📋 TEMPLATE STATUS', b'tm_status')],
            [Button.inline('⬅️ BACK TO CHANNELS', b'tm_back_channels')],
            [Button.inline('🗑️ DELETE CHANNEL', b'tm_delete_channel')],
            [Button.inline('❌ CANCEL', b'tm_cancel')],
        ]
        await event.respond(
            f'⚙️ CHANNEL MANAGER\n\n📛 {name}\n🆔 {all_channels().get(name)}\n\n'
            '🟢 = Telegram से custom template saved\n'
            '⚪ = अभी पुराना/default template चल रहा है\n\n'
            '➡️ जिस एक चीज को बदलना है, सिर्फ उसी button पर tap करो.',
            buttons=rows,
        )

    async def preview(event, s):
        draft = s.get('draft') or {}
        text = draft.get('text') or '[EMPTY MESSAGE]'
        emojis = draft.get('custom_emojis') or []
        await event.respond(
            f'👁️ PREVIEW\n\n📛 {s["channel"]}\n🎯 {label(s["kind"])}\n'
            '━━━━━━━━━━━━━━━━━━\n'
            f'{text}\n'
            '━━━━━━━━━━━━━━━━━━\n\n'
            f'😀 Fixed Custom Emoji: {len(emojis)}\n'
            '⚠️ अभी live template नहीं बदला है.\n'
            'सही है तो SAVE करो.',
            buttons=[
                [Button.inline('💾 SAVE', b'tm_save'), Button.inline('✏️ EDIT AGAIN', b'tm_edit_again')],
                [Button.inline('👁️ PREVIEW AGAIN', b'tm_preview_again'), Button.inline('❌ CANCEL', b'tm_cancel_draft')],
                [Button.inline('⬅️ BACK', b'tm_back_templates')],
            ],
        )

    async def prompt_template(event, s, kind):
        s['kind'] = kind; s['stage'] = 'waiting_template'; s.pop('draft', None); persist()
        current = get_channel_data(s['channel']) or {}
        current_tpl = (current.get('templates') or {}).get(kind)
        current_text = current_tpl.get('text') if isinstance(current_tpl, dict) else None
        await event.respond(
            f'✏️ EDIT — {label(kind)}\n\n📛 Channel: {s["channel"]}\n\n'
            + ('📌 CURRENT TEMPLATE:\n' + current_text + '\n\n' if current_text else '📌 अभी custom override नहीं है. पुराना/default template active है.\n\n')
            + f'🔤 Variables: {vars_for(kind)}\n\n'
            'अब नया पूरा message इसी chat में भेजो.\n'
            '📌 Custom/Premium emoji भी इसी message में भेज सकते हो.\n'
            '➡️ Message आते ही Preview मिलेगा.\n'
            '💾 SAVE करने तक पुराना template बिल्कुल नहीं बदलेगा.',
            buttons=[[Button.inline('⬅️ BACK', b'tm_back_templates'), Button.inline('❌ CANCEL', b'tm_cancel')]],
        )

    async def status(event, s):
        data = get_channel_data(s['channel']) or {}
        saved = set((data.get('templates') or {}).keys())
        lines = [f'📋 STATUS — {s["channel"]}', '']
        for kind, text, _ in TEMPLATE_STEPS:
            lines.append(f'{"🟢 CUSTOM" if kind in saved else "⚪ DEFAULT"} {text}')
        await event.respond('\n'.join(lines), buttons=template_rows(s['channel']) + [[Button.inline('⬅️ BACK', b'tm_back_templates')]])

    @bot.on(events.NewMessage(pattern=r'^/start$'))
    async def start(event):
        if not allowed(event): return
        await home(event)
        if state.get(owner_key):
            await event.respond('🔄 तुम्हारा पिछला काम सुरक्षित है.', buttons=[[Button.inline('▶️ RESUME', b'tm_resume')]])

    @bot.on(events.NewMessage(pattern=r'^/(addchannel|editchannel)$'))
    async def commands(event):
        if not allowed(event): return
        if event.raw_text == '/addchannel':
            state[owner_key] = {'mode':'add','stage':'name','data':{},'templates':{},'index':0}; persist()
            await event.respond('➕ NEW CHANNEL\n\nSTEP 1/3 — Channel NAME भेजो.\n\n⬅️ BACK   ❌ CANCEL', buttons=[[Button.inline('❌ CANCEL', b'tm_cancel')]])
        else:
            await show_channels(event)

    @bot.on(events.CallbackQuery())
    async def callbacks(event):
        if not allowed(event):
            await event.answer('Not authorized', alert=True); return
        data = event.data.decode('utf-8', 'ignore')
        refresh_state()
        s = state.get(owner_key)
        if data == 'tm_home': await event.answer(); await home(event); return
        if data == 'tm_help':
            await event.answer(); await event.respond('❓ HELP\n\n➕ NEW CHANNEL = नया channel\n✏️ EDIT CHANNEL = पुराने/new channel को खोलना\n\nChannel खोलकर किसी एक template पर tap करो. नया message भेजो → Preview → Save.\n\nSAVE से पहले कुछ भी live नहीं बदलता. CANCEL करने पर पुराना template ही रहता है.', buttons=[[Button.inline('⬅️ BACK', b'tm_home')]]); return
        if data == 'tm_edit_channels':
            await event.answer()
            await show_channels(event)
            return
        if data == 'tm_all_channels':
            await event.answer()
            await event.respond(
                f'📋 ALL CHANNELS\n\nकुल channels: {len(all_channels())}\n\nजिस channel को edit करना है उसे चुनो:',
                buttons=channel_rows('tm_all_channel'),
            )
            return
        if data == 'tm_back_channels':
            await event.answer()
            await show_channels(event)
            return
        if data == 'tm_new':
            state[owner_key]={'mode':'add','stage':'name','data':{},'templates':{},'index':0}; persist(); await event.answer(); await event.respond('➕ NEW CHANNEL\n\nSTEP 1/3 — Channel NAME भेजो.', buttons=[[Button.inline('❌ CANCEL',b'tm_cancel')]]); return
        if data == 'tm_cancel':
            state.pop(owner_key,None); persist(); await event.answer('Cancelled'); await event.respond('❌ CANCELLED\n\nकोई नया change save नहीं हुआ.'); await home(event); return
        # A channel button creates the edit state. Handle channel selection
        # BEFORE requiring an existing state; otherwise every fresh edit can
        # incorrectly show "No active setup".
        if data.startswith('tm_edit_channel:') or data.startswith('tm_all_channel:') or data.startswith('tm_channel:'):
            name = data.split(':', 1)[1]
            if name not in all_channels():
                await event.answer('Channel नहीं मिला. EDIT CHANNEL फिर से खोलो.', alert=True)
                return
            state[owner_key] = {'mode':'edit','channel':name,'stage':'menu'}
            s = state[owner_key]
            persist()
            await event.answer()
            await show_channel(event, s)
            return

        if not s:
            await event.answer('No active setup. /start दबाओ.', alert=True); return
        if data == 'tm_resume':
            await event.answer();
            if s.get('mode') == 'edit': await show_channel(event,s)
            elif s.get('stage') == 'name': await event.respond('STEP 1/3 — Channel NAME भेजो.', buttons=nav('tm_restart'))
            elif s.get('stage') == 'id': await event.respond('STEP 2/3 — Channel ID भेजो.', buttons=nav('tm_restart'))
            elif s.get('draft'): await preview(event,s)
            else: await event.respond('🔄 Resume नहीं हो सका. /addchannel या /editchannel चलाओ.')
            return
        if data.startswith('tm_kind:'):
            parts = data.split(':', 2)
            kind = parts[1] if len(parts) > 1 else ''
            button_channel = parts[2] if len(parts) > 2 else None
            if kind not in {x[0] for x in TEMPLATE_STEPS}:
                await event.answer('Invalid template', alert=True); return
            # Old buttons may not contain the channel name. New buttons do,
            # so we can reconstruct edit state even if the process restarted
            # or an older state file was cleared.
            if not s and button_channel:
                if button_channel in all_channels():
                    state[owner_key] = {'mode':'edit','channel':button_channel,'stage':'menu'}
                    s = state[owner_key]
                else:
                    await event.answer('Channel नहीं मिला. EDIT CHANNEL फिर से खोलो.', alert=True); return
            if not s or s.get('mode') != 'edit' or not s.get('channel'):
                await event.answer('Channel state missing. EDIT CHANNEL फिर से खोलो.', alert=True); return
            if button_channel and s.get('channel') != button_channel:
                s['channel'] = button_channel
            s['kind']=kind; persist(); await event.answer(); await prompt_template(event,s,kind); return
        if data == 'tm_back_templates':
            s['stage']='menu'; s.pop('draft',None); persist(); await event.answer(); await show_channel(event,s); return
        if data == 'tm_status': await event.answer(); await status(event,s); return
        if data == 'tm_preview_again': await event.answer(); await preview(event,s); return
        if data == 'tm_edit_again': s['stage']='waiting_template'; s.pop('draft',None); persist(); await event.answer(); await event.respond('✏️ नया message फिर से भेजो.', buttons=[[Button.inline('⬅️ BACK',b'tm_back_templates'),Button.inline('❌ CANCEL',b'tm_cancel')]]); return
        if data == 'tm_cancel_draft':
            s.pop('draft',None); s['stage']='menu'; persist(); await event.answer(); await event.respond('❌ Draft cancelled. पुराना template active है.'); await show_channel(event,s); return
        if data == 'tm_save':
            if not s.get('draft') or not s.get('kind'): await event.answer('Nothing to save',alert=True); return
            if s.get('mode') == 'edit':
                name=s['channel']; kind=s['kind']; save = s['draft']; existing=get_channel_data(name) or {'name':name,'id':all_channels().get(name),'templates':{}}
                # Merge only this edited template into the already-saved channel.
                # All previously customized templates remain untouched.
                templates = dict(existing.get('templates') or {})
                templates[kind] = save
                commit_channel(name, existing.get('id'), templates)
                CHANNELS[name]=int(existing.get('id'))
                s.pop('draft',None); s['stage']='menu'; persist()
                await event.answer('Saved'); await event.respond(f'💾 SAVED\n\n📛 {name}\n🎯 {label(kind)}\n\n✅ सिर्फ यही template बदला गया है. बाकी सब untouched है.\n\n➡️ अगला काम चुनो.', buttons=template_rows()+[[Button.inline('⬅️ BACK TO CHANNELS',b'tm_back_channels')],[Button.inline('🏠 MAIN MENU',b'tm_home')]])
                return
            # Add wizard: save one template then go next.
            s['templates'][s['kind']]=s['draft']; s['index'] += 1; s.pop('draft',None)
            if s['index'] >= len(TEMPLATE_STEPS):
                s['stage']='confirm'; persist(); await event.answer('All templates saved to draft'); await event.respond(f'🎉 ALL TEMPLATES READY\n\n📛 {s["data"]["name"]}\n🆔 {s["data"]["id"]}\n\n➡️ अब final SAVE CHANNEL दबाओ.', buttons=[[Button.inline('💾 SAVE CHANNEL',b'tm_save_channel')],[Button.inline('✏️ EDIT TEMPLATES',b'tm_edit_all')],[Button.inline('❌ CANCEL',b'tm_cancel')]]); return
            s['stage']='waiting_template'; kind,lab,var=TEMPLATE_STEPS[s['index']]; s['kind']=kind; persist(); await event.answer('Saved — next'); await event.respond(f'💾 {label(s["kind"])} SAVED\n\n➡️ NEXT: {s["index"]+1}/{len(TEMPLATE_STEPS)} — {lab}\n🔤 {var}\n\nअब message भेजो.', buttons=nav('tm_add_back'))
            return
        if data == 'tm_save_channel':
            if s.get('mode')!='add' or len(s.get('templates',{})) != len(TEMPLATE_STEPS): await event.answer('Setup अधूरा है',alert=True); return
            name=s['data']['name']; cid=s['data']['id']; commit_channel(name,cid,s['templates']); CHANNELS[name]=cid; state.pop(owner_key,None); persist(); await event.answer('Channel saved'); await event.respond(f'✅ CHANNEL SAVED\n\n📛 {name}\n🆔 {cid}\n\nअब यह channel भी बाकी channels की तरह edit हो सकता है.\n➡️ /editchannel से कभी भी किसी एक चीज को बदल सकते हो.'); await home(event); return
        if data == 'tm_edit_all':
            s['index']=0; s['stage']='waiting_template'; kind,lab,var=TEMPLATE_STEPS[0]; s['kind']=kind; s['templates']={}; persist(); await event.answer(); await event.respond(f'✏️ EDIT TEMPLATES\n\nSTEP 1/{len(TEMPLATE_STEPS)} — {lab}\n🔤 {var}\n\nMessage भेजो.', buttons=nav('tm_restart')); return
        if data == 'tm_add_back':
            if s.get('index',0) <= 0: await event.answer('यह पहला template है',alert=True); return
            s['index'] -= 1; kind,lab,var=TEMPLATE_STEPS[s['index']]; s['kind']=kind; s['stage']='waiting_template'; s['templates'].pop(kind,None); persist(); await event.answer(); await event.respond(f'⬅️ BACK\n\nअब {s["index"]+1}/{len(TEMPLATE_STEPS)} — {lab}\n🔤 {var}', buttons=nav('tm_add_back')); return
        if data == 'tm_restart':
            state[owner_key]={'mode':'add','stage':'name','data':{},'templates':{},'index':0}; persist(); await event.answer(); await event.respond('🔄 RESTARTED\n\nSTEP 1/3 — Channel NAME भेजो.', buttons=[[Button.inline('❌ CANCEL',b'tm_cancel')]]); return
        if data == 'tm_delete_channel':
            name=s['channel']; await event.answer(); await event.respond(f'⚠️ DELETE CHANNEL?\n\n📛 {name}\n\nयह सिर्फ saved configuration हटाएगा; Telegram channel delete नहीं होगा.', buttons=[[Button.inline('🗑️ YES, DELETE',f'tm_confirm_delete:{name}'.encode())],[Button.inline('⬅️ BACK',b'tm_back_templates'),Button.inline('❌ CANCEL',b'tm_cancel')]]); return
        if data.startswith('tm_confirm_delete:'):
            name=data.split(':',1)[1]; remove_dynamic_channel(name); s.pop('channel',None); state.pop(owner_key,None); persist(); CHANNELS.pop(name,None); await event.answer('Deleted'); await event.respond(f'🗑️ {name} configuration deleted.'); await home(event); return

    @bot.on(events.NewMessage())
    async def wizard(event):
        if not allowed(event): return
        refresh_state()
        if event.raw_text and event.raw_text.startswith('/'): return
        s=state.get(owner_key)
        if not s: return
        text=(event.raw_text or '').strip()
        if s.get('mode')=='add' and s.get('stage')=='name':
            if not text or any(c in text for c in ' /\\'):
                await event.respond('❌ Simple channel NAME भेजो.', buttons=[[Button.inline('❌ CANCEL',b'tm_cancel')]]); return
            name=text.upper()
            if name in all_channels(): await event.respond('❌ यह channel पहले से मौजूद है. दूसरा नाम भेजो.', buttons=nav('tm_restart')); return
            s['data']={'name':name}; s['stage']='id'; persist(); await event.respond(f'✅ NAME: {name}\n\nSTEP 2/3 — अब Channel ID भेजो.\nExample: -1001234567890', buttons=nav('tm_restart')); return
        if s.get('mode')=='add' and s.get('stage')=='id':
            try: cid=int(text); assert cid < 0
            except Exception: await event.respond('❌ सही Channel ID भेजो. Example: -1001234567890', buttons=nav('tm_restart')); return
            if cid in all_channels().values(): await event.respond('❌ यह Channel ID पहले से registered है.', buttons=nav('tm_restart')); return
            s['data']['id']=cid; s['stage']='waiting_template'; s['index']=0; s['kind']=TEMPLATE_STEPS[0][0]; persist(); kind,lab,var=TEMPLATE_STEPS[0]
            await event.respond(f'✅ CHANNEL ID SAVED\n\nSTEP 3/{len(TEMPLATE_STEPS)+2} — {lab}\n🔤 {var}\n\nअब पूरा message भेजो.\n➡️ फिर Preview → Save आएगा.', buttons=nav('tm_restart')); return
        if s.get('stage')=='waiting_template':
            if not event.raw_text and not event.media: await event.respond('❌ Message/text भेजो.', buttons=nav('tm_back_templates')); return
            s['draft']=save_template_data(event); s['stage']='preview'; persist(); await preview(event,s); return
        if s.get('stage')=='preview':
            await event.respond('👇 ऊपर Preview के नीचे SAVE / EDIT AGAIN / CANCEL में से चुनो.')

    print('✅ AUTO POST CONTROL BOT LOADED — persistent buttons/editor')
