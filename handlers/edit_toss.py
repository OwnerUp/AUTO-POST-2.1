# =========================================
# handlers/edit_toss.py
# =========================================

import re

from telethon import events

from memory.memory_manager import *

from utils import (
    edit_media_safe,
    edit_text_safe
)

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
)

import config


def register_edit_toss_handler(client):

    @client.on(events.NewMessage(pattern=r'^/etoss'))

    async def edit_toss_handler(event):

        me = await client.get_me()

        if event.chat_id != me.id:
            return

        raw = event.raw_text.strip()

        print("EDIT TOSS HIT")
        print(raw)

             # =========================================
        # FORMAT
        # /etoss 5 (INDIA WOMEN)
        # =========================================

        match = re.match(
            r'^/etoss\s+(\d+)\s+\((.*?)\)$',
            raw,
            re.IGNORECASE
        )

        if not match:

            await event.reply(
                "❌ WRONG FORMAT\n\nUSE:\n/etoss 5 (INDIA WOMEN)"
            )

            return

        toss_id = int(match.group(1))

        team = match.group(2).strip().upper()

        data = load_memory()

        selected = None

        for toss in data["tosses"]:

            if toss["id"] == toss_id:

                if toss.get("status") == "deleted":

                    await event.reply(
                        "❌ TOSS ALREADY DELETED"
                    )

                    return

                selected = toss

                break

        if not selected:

            await event.reply(
                "❌ TOSS ID NOT FOUND"
            )

            return

        print("EDIT ID :", toss_id)

        print("TEAM :", team)

             # =========================================
        # LOOP ALL CHANNELS
        # =========================================

        for post in selected["posts"]:

            channel = post["channel_id"]

            photo_id = post["photo_id"]

            promo_id = post["promo_id"]

            channel_name = post["channel_name"]

            print("CHANNEL :", channel_name)

            print("PHOTO :", photo_id)

            print("PROMO :", promo_id)

                        # =========================================
            # CREATE NEW CAPTION
            # =========================================

            team_name = team

            if channel_name == "ROYAL":
                caption, promo = royal_toss(team_name)

            elif channel_name == "BATMAN":
                caption, promo = batman_toss(team_name)

            elif channel_name == "BETTING":
                caption, promo = betting_toss(team_name, config.CURRENT_LEAGUE)

            elif channel_name == "GAME":
                caption, promo = game_toss(team_name, config.CURRENT_LEAGUE)

            elif channel_name == "GUDDU":
                caption, promo = guddu_toss(team_name, config.CURRENT_LEAGUE)

            elif channel_name == "ROCKY":
                caption, promo = rocky_toss(team_name)

            elif channel_name == "JACKY":
                caption, promo = jacky_toss(team_name, config.CURRENT_LEAGUE)

            elif channel_name == "PRIYANSHU":
                caption, promo = priyanshu_toss(team_name)

            elif channel_name == "TOSSKING":
                caption, promo = tossking_toss(team_name)

            elif channel_name == "REDDY":
                caption, promo = reddy_toss(team_name, config.CURRENT_LEAGUE)

            elif channel_name == "SHIVA":
                caption, promo = shiva_toss(team_name, config.CURRENT_LEAGUE)

            elif channel_name == "RAHUL":
                caption, promo = rahul_toss(team_name, config.CURRENT_LEAGUE)

            elif channel_name == "ANGAD":
                caption, promo = angad_toss(team_name)

            elif channel_name == "KING":
                caption, promo = king_toss(team_name, config.CURRENT_LEAGUE)

            else:

                caption = f"TOSS : {team_name}"
                promo = f"{team_name} WON THE TOSS"

            try:
                await edit_media_safe(
                    client,
                    channel,
                    photo_id,
                    caption,
                    channel_name
                )

                await edit_text_safe(
                    client,
                    channel,
                    promo_id,
                    promo,
                    channel_name
                )

            except Exception as e:
                print(f"{channel_name} : {e}")
                continue

    print("✅ EDIT TOSS HANDLER LOADED")      