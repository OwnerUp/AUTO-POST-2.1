# =========================================
# handlers/match_handler.py
# =========================================
from telethon import events
from emoji_parser import parse_match
from dynamic_emoji import (
    get_custom_emoji_entities,
    get_text_custom_emojis
)
import re

import config

from memory.memory_manager import *

from channels import CHANNELS

from utils import (

    send_media_safe,
    send_text_safe

)
from dynamic_render import render as render_dynamic

from templates.match_templates import (

    royal_match,
    batman_match,
    betting_match,
    game_match,
    guddu_match,
    rocky_match,
    jacky_match,
    priyanshu_match,
    tossking_match,
    reddy_match,
    shiva_match,
    rahul_match,
    angad_match,
    king_match,

    vikram_match,
    pawan_match,
    dubai_match,
    shubham_match,
    vikas_match,
    fixer_match,
)

# =========================================
# MEMORY
# =========================================

match_posts = []


# =========================================
# REGISTER
# =========================================

def register_match_handler(client):

    @client.on(events.NewMessage(pattern=r'^/match(?:\s|$)'))

    async def match_handler(event):

        print("MATCH COMMAND:", event.raw_text)

        custom_emojis = get_custom_emoji_entities(event)

        print(
             "🔥 MATCH CUSTOM EMOJIS:",
            custom_emojis
        )

        me = await client.get_me()

        if event.chat_id != me.id:
            return

        # =========================================
        # PARSE MATCH
        # =========================================

        print("RAW EXACT:", repr(event.raw_text))
        parsed = parse_match(event.raw_text)

        if not parsed:
            await event.reply(
                "❌ WRONG FORMAT\n\n"
                "USE:\n"
                "/match (INDIA WOMEN) VS (ENGLAND WOMEN) W (INDIA WOMEN)\n"
             )
            return

        team1, team2, winner = parsed
        print("PARSED OK:", team1, team2, winner)

        team1_custom_emojis = get_text_custom_emojis(
            event,
            team1,
            occurrence=1
        )

        team2_custom_emojis = get_text_custom_emojis(
            event,
            team2,
            occurrence=1
        )

        winner_occurrence = 2 if winner == team1 else 1

        winner_custom_emojis = get_text_custom_emojis(
            event,
            winner,
            occurrence=winner_occurrence
        )

        print("🔥 TEAM1 EMOJIS:", team1_custom_emojis)
        print("🔥 TEAM2 EMOJIS:", team2_custom_emojis)
        print("🔥 WINNER EMOJIS:", winner_custom_emojis)

        dynamic_items = [
            {
                "text": team1,
                "emojis": team1_custom_emojis
            },
            {
                "text": team2,
                "emojis": team2_custom_emojis
            }
        ]

        if winner != team1 and winner != team2:
            dynamic_items.append({
                "text": winner,
                "emojis": winner_custom_emojis
            })

        match_custom_emojis = get_custom_emoji_entities(event)

        print(
             "🔥 MATCH ENTITIES SAVE:",
         match_custom_emojis
        )

        if not event.reply_to_msg_id:
            await event.reply("REPLY TO PHOTO")
            return

        reply_msg = await event.get_reply_message()
        print("PHOTO OK")

        ids = []

        # =====================================
        # LOOP CHANNELS
        # =====================================

        for channel_name, channel in CHANNELS.items():

            dyn = render_dynamic(channel_name, "match", {"TEAM1": team1, "TEAM2": team2, "WINNER": winner, "LEAGUE": config.CURRENT_LEAGUE})
            dyn_p1 = render_dynamic(channel_name, "match_promo1", {"TEAM1": team1, "TEAM2": team2, "WINNER": winner, "LEAGUE": config.CURRENT_LEAGUE})
            dyn_p2 = render_dynamic(channel_name, "match_promo2", {"TEAM1": team1, "TEAM2": team2, "WINNER": winner, "LEAGUE": config.CURRENT_LEAGUE})
            # Main / promo1 / promo2 are independently overridable.
            if dyn or dyn_p1 or dyn_p2:
                legacy = None
                if channel_name == "ROYAL": legacy = royal_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "BATMAN": legacy = batman_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "BETTING": legacy = betting_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "GAME": legacy = game_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "GUDDU": legacy = guddu_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "ROCKY": legacy = rocky_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "JACKY": legacy = jacky_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "PRIYANSHU": legacy = priyanshu_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "TOSSKING": legacy = tossking_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "REDDY": legacy = reddy_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "SHIVA": legacy = shiva_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "RAHUL": legacy = rahul_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "ANGAD": legacy = angad_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "KING": legacy = king_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "VIKRAM": legacy = vikram_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "PAWAN": legacy = pawan_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "DUBAI": legacy = dubai_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "SHUBHAM": legacy = shubham_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "VIKAS": legacy = vikas_match(team1, team2, winner, config.CURRENT_LEAGUE)
                elif channel_name == "FIXER": legacy = fixer_match(team1, team2, winner, config.CURRENT_LEAGUE)
                if dyn:
                    text, template_entities = dyn
                else:
                    text, template_entities = (legacy[0], []) if legacy else ('', [])
                if dyn_p1:
                    p1, p1_entities = dyn_p1
                else:
                    p1, p1_entities = (legacy[1], []) if legacy else (None, [])
                if dyn_p2:
                    p2, p2_entities = dyn_p2
                else:
                    p2, p2_entities = (legacy[2], []) if legacy else (None, [])
                msg = await send_media_safe(client, channel, reply_msg, text, channel_name, dynamic_items=dynamic_items, template_entities=template_entities)
                promo1 = await send_text_safe(client, channel, p1, msg.id, channel_name, dynamic_items=dynamic_items, template_entities=p1_entities) if p1 else None
                promo2 = await send_text_safe(client, channel, p2, promo1.id if promo1 else msg.id, channel_name, dynamic_items=dynamic_items, template_entities=p2_entities) if p2 else None
                ids.append({"channel_id": channel, "photo_id": msg.id, "promo1_id": promo1.id if promo1 else None, "promo2_id": promo2.id if promo2 else None, "channel_name": channel_name})
                continue

            # =================================
            # ROYAL
            # =================================

            if channel_name == "ROYAL":

                text, promo1, promo2 = royal_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # BATMAN
            # =================================

            elif channel_name == "BATMAN":

                text, promo1, promo2 = batman_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # BETTING
            # =================================

            elif channel_name == "BETTING":

                text, promo1, promo2 = betting_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # GAME
            # =================================

            elif channel_name == "GAME":

                text, promo1, promo2 = game_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # GUDDU
            # =================================

            elif channel_name == "GUDDU":

                text, promo1, promo2 = guddu_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # ROCKY
            # =================================

            elif channel_name == "ROCKY":

                text, promo1, promo2 = rocky_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # JACKY
            # =================================

            elif channel_name == "JACKY":

                text, promo1, promo2 = jacky_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # PRIYANSHU
            # =================================

            elif channel_name == "PRIYANSHU":

                text, promo1, promo2 = priyanshu_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # TOSSKING
            # =================================

            elif channel_name == "TOSSKING":

                text, promo1, promo2 = tossking_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # REDDY
            # =================================

            elif channel_name == "REDDY":

                text, promo1, promo2 = reddy_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # SHIVA
            # =================================

            elif channel_name == "SHIVA":

                text, promo1, promo2 = shiva_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )
                            # =================================
            # RAHUL
            # =================================

            elif channel_name == "RAHUL":

                text, promo1, promo2 = rahul_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # ANGAD
            # =================================

            elif channel_name == "ANGAD":

                text, promo1, promo2 = angad_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # KING
            # =================================

            elif channel_name == "KING":

                text, promo1, promo2 = king_match(

                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # VIKRAM
            # =================================

            elif channel_name == "VIKRAM":

                text, promo1, promo2 = vikram_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # PAWAN
            # =================================

            elif channel_name == "PAWAN":

                text, promo1, promo2 = pawan_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # DUBAI
            # =================================

            elif channel_name == "DUBAI":

                text, promo1, promo2 = dubai_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # SHUBHAM
            # =================================

            elif channel_name == "SHUBHAM":

                text, promo1, promo2 = shubham_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # VIKAS
            # =================================

            elif channel_name == "VIKAS":

                text, promo1, promo2 = vikas_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            # =================================
            # FIXER
            # =================================

            elif channel_name == "FIXER":

                text, promo1, promo2 = fixer_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            else:
                continue

            # =================================
            # SEND MEDIA
            # =================================

            msg = await send_media_safe(
                client,
                channel,
                reply_msg,
                text,
                channel_name,
                dynamic_items=dynamic_items
            )

            # =================================
            # SEND PROMO 1
            # =================================

            promo1_msg = await send_text_safe(
                client,
                channel,
                promo1,
                msg.id,
                channel_name,
                dynamic_items=dynamic_items
            )

            # =================================
            # SEND PROMO 2
            # =================================

            promo2_msg = None

            if promo2:

                promo2_msg = await send_text_safe(
                    client,
                    channel,
                    promo2,
                    msg.id,
                    channel_name,
                    dynamic_items=dynamic_items
                )

            ids.append({

                "channel_id": channel,

                "photo_id": msg.id,

                "promo1_id": promo1_msg.id,

                "promo2_id": promo2_msg.id if promo2_msg else None,

                "channel_name": channel_name

            })

        # =========================
        # SAVE MATCH TO MEMORY
        # =========================

        data = load_memory()

        new_match = {
        "id": get_next_id("matches"),
        "team1": team1,
        "team2": team2,
        "winner": winner,
        "status": "pending",
        "posts": ids
}

        data["matches"].append(new_match)

        save_memory(data)

        print(f"\n✅ MATCH SAVED : ID {new_match['id']}\n")

        match_posts.append(ids)

        await event.reply(

            f"✅ MATCH POSTED\n🆔 ID : {new_match['id']}"
        )

print("✅ MATCH HANDLER LOADED")