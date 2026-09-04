# =========================================
# handlers/toss_handler.py
# =========================================

from dynamic_emoji import (
    get_custom_emoji_entities,
    get_toss_team_custom_emojis
)
from emoji_parser import parse_toss_team
from telethon import events
import re

import config
from channels import CHANNELS
from memory.memory_manager import *

from utils import (
    send_media_safe,
    send_text_safe
)
from dynamic_render import render as render_dynamic

from templates.toss_templates import (
    royal_toss,
    batman_toss,
    betting_toss,
    game_toss,
    guddu_toss,
    rocky_toss,
    jacky_toss,
    priyanshu_toss,
    tossking_toss,
    reddy_toss,
    shiva_toss,
    rahul_toss,
    angad_toss,
    king_toss,

    vikram_toss,
    pawan_toss,
    dubai_toss,
    shubham_toss,
    vikas_toss,
    fixer_toss,
)

toss_posts = []

def register_toss_handler(client):

    @client.on(events.NewMessage(pattern='/toss'))
    async def toss_handler(event):
        custom_emojis = get_custom_emoji_entities(event)
        print("🔥 CUSTOM EMOJIS:", custom_emojis)

        me = await client.get_me()

        if event.chat_id != me.id:
            return

        # =========================
        # PARSE TEAM WITH EMOJI
        # =========================

        team = parse_toss_team(event.raw_text)

        if not team:
            await event.reply(
            "❌ WRONG FORMAT\n\n"
            "USE:\n"
            "/toss (INDIA WOMEN)\n"
            )
            return
        
        team_custom_emojis = get_toss_team_custom_emojis(
            event,
            team
        )

        print(
            "🔥 TEAM CUSTOM EMOJIS:",
            team_custom_emojis
        )

        # =========================
        # CHECK PHOTO REPLY
        # =========================

        if not event.reply_to_msg_id:
            await event.reply("REPLY TO PHOTO")
            return

        reply_msg = await event.get_reply_message()

        ids = []

        # =========================
        # SEND TO ALL CHANNELS
        # =========================

        for channel_name, channel in CHANNELS.items():

            dyn = render_dynamic(channel_name, "toss", {"TEAM": team, "LEAGUE": config.CURRENT_LEAGUE})
            dyn_promo = render_dynamic(channel_name, "toss_promo", {"TEAM": team, "LEAGUE": config.CURRENT_LEAGUE})
            # Main and promo are independently overridable. Editing only one
            # must never reset or bypass the other.
            if dyn or dyn_promo:
                if dyn:
                    caption, template_entities = dyn
                else:
                    caption, promo_fallback = None, None
                if dyn_promo:
                    promo, promo_entities = dyn_promo
                else:
                    promo, promo_entities = None, []

                if caption is None:
                    # Keep the legacy/code template for the untouched part.
                    legacy = None
                    if channel_name == "ROYAL": legacy = royal_toss(team)
                    elif channel_name == "BATMAN": legacy = batman_toss(team)
                    elif channel_name == "BETTING": legacy = betting_toss(team, config.CURRENT_LEAGUE)
                    elif channel_name == "GAME": legacy = game_toss(team, config.CURRENT_LEAGUE)
                    elif channel_name == "GUDDU": legacy = guddu_toss(team, config.CURRENT_LEAGUE)
                    elif channel_name == "ROCKY": legacy = rocky_toss(team)
                    elif channel_name == "JACKY": legacy = jacky_toss(team)
                    elif channel_name == "PRIYANSHU": legacy = priyanshu_toss(team)
                    elif channel_name == "TOSSKING": legacy = tossking_toss(team)
                    elif channel_name == "REDDY": legacy = reddy_toss(team, config.CURRENT_LEAGUE)
                    elif channel_name == "SHIVA": legacy = shiva_toss(team, config.CURRENT_LEAGUE)
                    elif channel_name == "RAHUL": legacy = rahul_toss(team, config.CURRENT_LEAGUE)
                    elif channel_name == "ANGAD": legacy = angad_toss(team)
                    elif channel_name == "KING": legacy = king_toss(team, config.CURRENT_LEAGUE)
                    elif channel_name == "VIKRAM": legacy = vikram_toss(team)
                    elif channel_name == "PAWAN": legacy = pawan_toss(team)
                    elif channel_name == "DUBAI": legacy = dubai_toss(team, config.CURRENT_LEAGUE)
                    elif channel_name == "SHUBHAM": legacy = shubham_toss(team)
                    elif channel_name == "VIKAS": legacy = vikas_toss(team)
                    elif channel_name == "FIXER": legacy = fixer_toss(team)
                    if legacy:
                        caption = legacy[0]
                msg = await send_media_safe(client, channel, reply_msg, caption, channel_name, dynamic_team=team, dynamic_emojis=team_custom_emojis, template_entities=(template_entities if dyn else None))
                promo_msg = None
                if not dyn_promo:
                    # Untouched promo remains exactly as before.
                    if channel_name == "ROYAL": promo = royal_toss(team)[1]
                    elif channel_name == "BATMAN": promo = batman_toss(team)[1]
                    elif channel_name == "BETTING": promo = betting_toss(team, config.CURRENT_LEAGUE)[1]
                    elif channel_name == "GAME": promo = game_toss(team, config.CURRENT_LEAGUE)[1]
                    elif channel_name == "GUDDU": promo = guddu_toss(team, config.CURRENT_LEAGUE)[1]
                    elif channel_name == "ROCKY": promo = rocky_toss(team)[1]
                    elif channel_name == "JACKY": promo = jacky_toss(team)[1]
                    elif channel_name == "PRIYANSHU": promo = priyanshu_toss(team)[1]
                    elif channel_name == "TOSSKING": promo = tossking_toss(team)[1]
                    elif channel_name == "REDDY": promo = reddy_toss(team, config.CURRENT_LEAGUE)[1]
                    elif channel_name == "SHIVA": promo = shiva_toss(team, config.CURRENT_LEAGUE)[1]
                    elif channel_name == "RAHUL": promo = rahul_toss(team, config.CURRENT_LEAGUE)[1]
                    elif channel_name == "ANGAD": promo = angad_toss(team)[1]
                    elif channel_name == "KING": promo = king_toss(team, config.CURRENT_LEAGUE)[1]
                    elif channel_name == "VIKRAM": promo = vikram_toss(team)[1]
                    elif channel_name == "PAWAN": promo = pawan_toss(team)[1]
                    elif channel_name == "DUBAI": promo = dubai_toss(team, config.CURRENT_LEAGUE)[1]
                    elif channel_name == "SHUBHAM": promo = shubham_toss(team)[1]
                    elif channel_name == "VIKAS": promo = vikas_toss(team)[1]
                    elif channel_name == "FIXER": promo = fixer_toss(team)[1]
                if promo:
                    promo_msg = await send_text_safe(client, channel, promo, msg.id, channel_name, dynamic_team=team, dynamic_emojis=team_custom_emojis, template_entities=(promo_entities if dyn_promo else None))
                ids.append({"channel_id": channel, "photo_id": msg.id, "promo_id": promo_msg.id if promo_msg else None, "channel_name": channel_name})
                continue

            if channel_name == "ROYAL":
                caption, promo = royal_toss(team)

            elif channel_name == "BATMAN":
                caption, promo = batman_toss(team)

            elif channel_name == "BETTING":
                caption, promo = betting_toss(team, config.CURRENT_LEAGUE)

            elif channel_name == "GAME":
                caption, promo = game_toss(team, config.CURRENT_LEAGUE)

            elif channel_name == "GUDDU":
                caption, promo = guddu_toss(team, config.CURRENT_LEAGUE)

            elif channel_name == "ROCKY":
                caption, promo = rocky_toss(team)

            elif channel_name == "JACKY":
                caption, promo = jacky_toss(team, config.CURRENT_LEAGUE)

            elif channel_name == "PRIYANSHU":
                caption, promo = priyanshu_toss(team)

            elif channel_name == "TOSSKING":
                caption, promo = tossking_toss(team)

            elif channel_name == "REDDY":
                caption, promo = reddy_toss(team, config.CURRENT_LEAGUE)

            elif channel_name == "SHIVA":
                caption, promo = shiva_toss(team, config.CURRENT_LEAGUE)

            elif channel_name == "RAHUL":
                caption, promo = rahul_toss(team, config.CURRENT_LEAGUE)

            elif channel_name == "ANGAD":
                caption, promo = angad_toss(team)

            elif channel_name == "KING":
                caption, promo = king_toss(team, config.CURRENT_LEAGUE)

            elif channel_name == "VIKRAM":
                caption, promo = vikram_toss(team)

            elif channel_name == "PAWAN":
                caption, promo = pawan_toss(team)

            elif channel_name == "DUBAI":
                caption, promo = dubai_toss(team, config.CURRENT_LEAGUE)

            elif channel_name == "SHUBHAM":
                caption, promo = shubham_toss(team)

            elif channel_name == "VIKAS":
                caption, promo = vikas_toss(team)

            elif channel_name == "FIXER":
                caption, promo = fixer_toss(team)

            else:
                continue

            msg = await send_media_safe(
              client,
             channel,
             reply_msg,
             caption,
             channel_name,
             team,
             team_custom_emojis
            )

            promo_msg = await send_text_safe(
            client,
            channel,
            promo,
            msg.id,
            channel_name,
            team,
            team_custom_emojis
            )
            
            ids.append({
                "channel_id": channel,
                "photo_id": msg.id,
                "promo_id": promo_msg.id,
                "channel_name": channel_name
            })

        # =========================
        # SAVE TO MEMORY
        # =========================

        data = load_memory()

        new_toss = {
            "id": get_next_id("tosses"),
            "match": team,
            "winner": team,
            "status": "pending",
            "posts": ids
        }

        data["tosses"].append(new_toss)
        save_memory(data)

        await event.reply(
            f"✅ TOSS POSTED\n🆔 ID : {new_toss['id']}"
        )

print("✅ TOSS HANDLER LOADED")