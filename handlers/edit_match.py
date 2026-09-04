# =========================================
# handlers/edit_match.py
# =========================================

import re

from telethon import events

from memory.memory_manager import *

from utils import (
    edit_media_safe,
    edit_text_safe
)

import config

from templates.match_templates import *


def register_edit_match_handler(client):

    @client.on(events.NewMessage(pattern=r'^/ematch'))

    async def edit_match_handler(event):

        me = await client.get_me()

        if event.chat_id != me.id:
            return

        raw = event.raw_text.strip()

        print("EDIT MATCH HIT")
        print(raw)

        # =========================================
        # FORMAT
        # /ematch 5 (TEAM1) VS (TEAM2) W (WINNER)
        # =========================================

        match = re.match(
            r'^/ematch\s+(\d+)\s+\((.*?)\)\s+VS\s+\((.*?)\)\s+W\s+\((.*?)\)$',
            raw,
            re.IGNORECASE
        )

        if not match:

            await event.reply(
                "❌ WRONG FORMAT\n\nUSE:\n/ematch 5 (INDIA) VS (PAKISTAN) W (INDIA)"
            )

            return

        match_id = int(match.group(1))

        team1 = match.group(2).strip().upper()

        team2 = match.group(3).strip().upper()

        winner = match.group(4).strip().upper()

        data = load_memory()

        selected = None

        for m in data["matches"]:

            if m["id"] == match_id:

                if m.get("status") == "deleted":

                    await event.reply(
                        "❌ MATCH ALREADY DELETED"
                    )

                    return

                selected = m

                break

        if not selected:

            await event.reply(
                "❌ MATCH ID NOT FOUND"
            )

            return

        print("MATCH ID :", match_id)
        print("TEAM1 :", team1)
        print("TEAM2 :", team2)
        print("WINNER :", winner)

        # =========================================
        # LOOP ALL CHANNELS
        # =========================================

        for post in selected["posts"]:

            channel = post["channel_id"]

            photo_id = post["photo_id"]

            promo1_id = post["promo1_id"]

            promo2_id = post["promo2_id"]

            channel_name = post["channel_name"]

            print("CHANNEL :", channel_name)

            print("PHOTO :", photo_id)

            print("PROMO1 :", promo1_id)

            print("PROMO2 :", promo2_id)

                        # =====================================
            # CREATE TEMPLATE
            # =====================================

            if channel_name == "ROYAL":

                caption, promo1, promo2 = royal_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "BATMAN":

                caption, promo1, promo2 = batman_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "BETTING":

                caption, promo1, promo2 = betting_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "GAME":

                caption, promo1, promo2 = game_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "GUDDU":

                caption, promo1, promo2 = guddu_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "ROCKY":

                caption, promo1, promo2 = rocky_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "JACKY":

                caption, promo1, promo2 = jacky_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )
            elif channel_name == "PRIYANSHU":

                caption, promo1, promo2 = priyanshu_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "TOSSKING":

                caption, promo1, promo2 = tossking_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "REDDY":

                caption, promo1, promo2 = reddy_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "SHIVA":

                caption, promo1, promo2 = shiva_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "RAHUL":

                caption, promo1, promo2 = rahul_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "ANGAD":

                caption, promo1, promo2 = angad_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            elif channel_name == "KING":

                caption, promo1, promo2 = king_match(
                    team1,
                    team2,
                    winner,
                    config.CURRENT_LEAGUE
                )

            else:

                caption = f"{team1} 🆚 {team2}"

                promo1 = f"WINNER : {winner}"

                promo2 = None

            # =====================================
            # EDIT PHOTO
            # =====================================

            await edit_media_safe(
                client,
                channel,
                photo_id,
                caption,
                channel_name
            )

            # =====================================
            # EDIT PROMO 1
            # =====================================

            await edit_text_safe(
                client,
                channel,
                promo1_id,
                promo1,
                channel_name
            )

            # =====================================
            # EDIT PROMO 2
            # =====================================

            if promo2_id and promo2:

                await edit_text_safe(
                    client,
                    channel,
                    promo2_id,
                    promo2,
                    channel_name
                )
        # =====================================
        # UPDATE MEMORY
        # =====================================

        selected["team1"] = team1
        selected["team2"] = team2
        selected["winner"] = winner

        save_memory(data)

        await event.reply(
            f"✅ MATCH EDITED\n🆔 ID : {match_id}"
        )


print("✅ EDIT MATCH HANDLER LOADED")