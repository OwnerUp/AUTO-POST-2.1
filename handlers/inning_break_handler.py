from telethon import events
import re

from memory.memory_manager import *
from utils import send_media_safe
from dynamic_render import render as render_dynamic

from templates.inning_break_templates import *

def register_inning_break_handler(client):

    @client.on(events.NewMessage(pattern=r'^/break'))

    async def inning_break_handler(event):

        me = await client.get_me()

        if event.chat_id != me.id:
            return

        print("INNING BREAK HIT")
        print(event.raw_text)

        # =====================================
        # PHOTO CHECK
        # =====================================

        if not event.reply_to_msg_id:
            await event.reply("❌ REPLY TO PHOTO")
            return

        reply_msg = await event.get_reply_message()

        print("PHOTO OK")


        # =========================
        # PARSE COMMAND
        # =========================

        raw = event.raw_text.strip()

        m = re.match(
            r'^/break\s+(\d+)\s+(\d+)\s+(chase|defend)\s+\((.*?)\)$',
            raw,
            re.IGNORECASE
        )

        if not m:
            await event.reply(
                "❌ WRONG FORMAT\n\n"
                "USE:\n"
                "/break 17 175 chase (NEW ZEALAND 🇳🇿)"
            )
            return

        match_id = int(m.group(1))
        target = m.group(2)
        prediction = m.group(3).lower()
        winner = m.group(4).strip().upper()

        print("MATCH ID :", match_id)
        print("TARGET :", target)
        print("PREDICTION :", prediction)
        print("WINNER :", winner)

        data = load_memory()

        selected = None

        for match in data["matches"]:

            if match["id"] == match_id:

                selected = match["posts"]

                print("SELECTED =", selected)

                break

        if not selected:
            await event.reply("❌ MATCH ID NOT FOUND")
            return
        print("TOTAL POSTS =", len(selected))

        # =====================================
        # LOOP CHANNELS
        # =====================================

        for post in selected:

            channel = post["channel_id"]
            channel_name = post["channel_name"]

            dyn = render_dynamic(channel_name, "break", {"TARGET": target, "PREDICTION": prediction, "WINNER": winner})
            if dyn:
                text, template_entities = dyn
                await send_media_safe(client, channel, reply_msg, text, channel_name, reply_to=post["photo_id"], template_entities=template_entities)
                continue

                        # =====================================
            # SELECT TEMPLATE
            # =====================================

            if channel_name == "ROYAL":
                text = royal_inning_break(target, prediction, winner)

            elif channel_name == "BATMAN":
                text = batman_inning_break(target, prediction, winner)

            elif channel_name == "BETTING":
                text = betting_inning_break(target, prediction, winner)

            elif channel_name == "GAME":
                text = game_inning_break(target, prediction, winner)

            elif channel_name == "GUDDU":
                text = guddu_inning_break(target, prediction, winner)

            elif channel_name == "ROCKY":
                text = rocky_inning_break(target, prediction, winner)

            elif channel_name == "JACKY":
                text = jacky_inning_break(target, prediction, winner)

            elif channel_name == "PRIYANSHU":
                text = priyanshu_inning_break(target, prediction, winner)

            elif channel_name == "TOSSKING":
                text = tossking_inning_break(target, prediction, winner)

            elif channel_name == "REDDY":
                text = reddy_inning_break(target, prediction, winner)

            elif channel_name == "SHIVA":
                text = shiva_inning_break(target, prediction, winner)

            elif channel_name == "RAHUL":
                text = rahul_inning_break(target, prediction, winner)

            elif channel_name == "ANGAD":
                text = angad_inning_break(target, prediction, winner)

            elif channel_name == "KING":
                text = king_inning_break(target, prediction, winner)

            elif channel_name == "VIKRAM":
                text = vikram_inning_break(target, prediction, winner)

            elif channel_name == "PAWAN":
                text = pawan_inning_break(target, prediction, winner)

            elif channel_name == "DUBAI":
                text = dubai_inning_break(target, prediction, winner)

            elif channel_name == "SHUBHAM":
                text = shubham_inning_break(target, prediction, winner)

            elif channel_name == "VIKAS":
                text = vikas_inning_break(target, prediction, winner)

            elif channel_name == "FIXER":
                text = fixer_inning_break(target, prediction, winner)

            else:
                continue

            # =====================================
            # SEND PHOTO + INNING BREAK
            # =====================================

            await send_media_safe(
                client,
                channel,
                reply_msg,
                text,
                channel_name,
                reply_to=post["photo_id"]
                )

        # =====================================
        # DONE
        # =====================================

        await event.reply("✅ INNING BREAK POSTED")