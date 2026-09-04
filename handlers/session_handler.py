# =========================================
# handlers/session_handler.py
# =========================================

from telethon import events

from channels import CHANNELS

from memory.memory_manager import *

from utils import send_media_safe
from dynamic_render import render as render_dynamic

from templates.session_templates import *

session_posts = []


def register_session_handler(client):

    @client.on(events.NewMessage(pattern='/session'))

    async def session_handler(event):

        me = await client.get_me()

        if event.chat_id != me.id:
           return

        raw = event.raw_text.replace(
            '/session',
            ''
        ).strip()

        cmd = raw.split()

        if len(cmd) != 3:

            await event.reply(
                "USE:\n/session 6 YES 52"
            )

            return

        over = cmd[0]

        call = cmd[1].upper()

        run = cmd[2]

        if call not in ["YES", "NOT"]:

            await event.reply(
                "CALL MUST BE YES OR NOT"
            )

            return

        if not event.reply_to_msg_id:

            await event.reply(
                "REPLY TO PHOTO"
            )

            return

        reply_msg = await event.get_reply_message()

        ids = []

        for channel_name, channel in CHANNELS.items():

            dyn = render_dynamic(channel_name, "session", {"OVER": over, "RUN": run, "CALL": call, "CALL_EMOJI": "✅" if call == "YES" else "❌"})
            if dyn:
                text, template_entities = dyn
                msg = await send_media_safe(client, channel, reply_msg, text, channel_name, template_entities=template_entities)
                ids.append({"channel_id": channel, "msg_id": msg.id, "channel_name": channel_name})
                continue

            if channel_name == "ROYAL":

                text = royal_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "BETTING":

                text = betting_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "BATMAN":

                text = batman_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "GAME":

                text = game_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "GUDDU":

                text = guddu_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "ROCKY":

                text = rocky_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "PRIYANSHU":

                text = priyanshu_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "JACKY":

                text = jacky_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "KING":

                text = king_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "ANGAD":

                text = angad_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "RAHUL":

                text = rahul_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "SHIVA":

                text = shiva_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "REDDY":

                text = reddy_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "TOSSKING":

                text = tossking_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "VIKRAM":

                text = vikram_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "PAWAN":

                text = pawan_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "DUBAI":

                text = dubai_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "SHUBHAM":

                text = shubham_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "VIKAS":

                text = vikas_session(
                    over,
                    run,
                    call
                )

            elif channel_name == "FIXER":

                text = fixer_session(
                    over,
                    run,
                    call
                )

            else:

                continue

            msg = await send_media_safe(
                client,
                channel,
                reply_msg,
                text,
                channel_name
            )

            ids.append({
                "channel_id": channel,
                "msg_id": msg.id,
                "channel_name": channel_name
            })

        # =========================
        # SAVE SESSION
        # =========================

        data = load_memory()

        new_session = {
            "id": get_next_id("sessions"),
            "over": over,
            "run": run,
            "call": call,
            "status": "pending",
            "posts": ids
        }

        data["sessions"].append(new_session)

        save_memory(data)

        print(
            f"\n✅ SESSION SAVED : ID {new_session['id']}\n"
        )

        session_posts.append(ids)

        await event.reply(
            f"✅ SESSION POSTED\n🆔 ID : {new_session['id']}"
        )


print("✅ SESSION HANDLER LOADED")