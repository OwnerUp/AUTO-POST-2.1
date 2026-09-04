from telethon import events

from channels import CHANNELS

from memory.memory_manager import *

from templates.sball_templates import *

from utils import send_media_safe
from dynamic_render import render as render_dynamic


session_posts = []


def register_sball_handler(client):

    @client.on(events.NewMessage(pattern='/sball'))

    async def sball_handler(event):

        me = await client.get_me()

        if event.chat_id != me.id:
            return

        raw = event.raw_text.replace(
            '/sball',
            ''
        ).strip()

        cmd = raw.split()

        if len(cmd) != 3:

            await event.reply(
                "USE:\n/sball 3 YES 12"
            )

            return

        ball = cmd[0]

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

            dyn = render_dynamic(channel_name, "sball", {"BALL": ball, "RUN": run, "CALL": call, "CALL_EMOJI": "✅" if call == "YES" else "❌"})
            if dyn:
                text, template_entities = dyn
                msg = await send_media_safe(client, channel, reply_msg, text, channel_name, template_entities=template_entities)
                ids.append({"channel_id": channel, "msg_id": msg.id, "channel_name": channel_name})
                continue

            if channel_name == "ROYAL":

               text = royal_sball(ball, run, call)

            elif channel_name == "BETTING":

                text = betting_sball(
                    ball,
                    run,
                    call
                )

            elif channel_name == "BATMAN":

                text = batman_sball(
                    ball,
                    run,
                    call
                )

            elif channel_name == "GAME":

                text = game_sball(
                    ball,
                    run,
                    call
                )

            elif channel_name == "GUDDU":

                text = guddu_sball(
                    ball,
                    run,
                    call
                )

            elif channel_name == "ROCKY":

                text = rocky_sball(
                    ball,
                    run,
                    call
                )

            elif channel_name == "PRIYANSHU":

                text = priyanshu_sball(
                    ball,
                    run,
                    call
                )

            elif channel_name == "JACKY":

                text = jacky_sball(
                    ball,
                    run,
                    call
                )

            elif channel_name == "KING":

                text = king_sball(
                    ball,
                    run,
                    call
                )

            elif channel_name == "ANGAD":

                text = angad_sball(
                    ball,
                    run,
                    call
                )

            elif channel_name == "RAHUL":

                text = rahul_sball(
                    ball,
                    run,
                    call
                )

            elif channel_name == "SHIVA":

                text = shiva_sball(
                    ball,
                    run,
                    call
                )

            elif channel_name == "REDDY":

                text = reddy_sball(
                    ball,
                    run,
                    call
                )

            elif channel_name == "TOSSKING":

                text = tossking_sball(
                    ball,
                    run,
                    call
                )

            elif channel_name == "VIKRAM":

                text = vikram_sball(
                    ball,
                    run,
                    call
                )

            elif channel_name == "PAWAN":

                text = pawan_sball(
                    ball,
                    run,
                    call
                )

            elif channel_name == "DUBAI":

                text = dubai_sball(
                    ball,
                    run,
                    call
                )

            elif channel_name == "SHUBHAM":

                text = shubham_sball(
                    ball,
                    run,
                    call
                )

            elif channel_name == "VIKAS":

                text = vikas_sball(
                    ball,
                    run,
                    call
                )

            elif channel_name == "FIXER":

                text = fixer_sball(
                    ball,
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
        # SAVE SBALL SESSION
        # =========================

        data = load_memory()

        new_session = {
            "id": get_next_id("sballs"),
            "ball": ball,
            "run": run,
            "call": call,
            "type": "ball",
            "status": "pending",
            "posts": ids
        }

        data["sballs"].append(new_session)

        save_memory(data)

        print(
            f"\n✅ SBALL SESSION SAVED : ID {new_session['id']}\n"
        )

        session_posts.append(ids)

        await event.reply(
            f"✅ BALL SESSION POSTED\n🆔 ID : {new_session['id']}"
        )