# =========================================
# handlers/sbpass_handler.py
# =========================================

from telethon import events

from memory.memory_manager import *

from templates import sball_templates

from utils import send_text_safe
from dynamic_render import render as render_dynamic



def register_sbpass_handler(client):

    @client.on(events.NewMessage(pattern='/sbpass'))

    async def sbpass_handler(event):

        me = await client.get_me()

        if event.chat_id != me.id:
            return

        raw = event.raw_text.replace(
            '/sbpass',
            ''
        ).strip()

        parts = raw.split()

        if len(parts) != 2:

            await event.reply(
                "USE:\n/sbpass 1 12"
            )

            return

        session_id = int(parts[0])

        result = parts[1]

        data = load_memory()

        target_session = None

        for session in data["sballs"]:

            if session["id"] == session_id:

                if session["status"] == "passed":

                    await event.reply(
                        "❌ BALL SESSION ALREADY PASSED"
                    )

                    return

                target_session = session

                break

        if not target_session:

            await event.reply(
                "BALL SESSION ID NOT FOUND"
            )

            return

        for post in target_session["posts"]:

            channel = post["channel_id"]

            msg_id = post["msg_id"]

            channel_name = post["channel_name"]

            dyn = render_dynamic(channel_name, "sball_pass", {"BALL": target_session["ball"], "RESULT": result})
            if dyn:
                text, template_entities = dyn
                await send_text_safe(client, channel, text, msg_id, channel_name, template_entities=template_entities)
                continue

            if channel_name == "ROYAL":

                text = sball_templates.royal_sball_pass(
                        target_session["ball"],
                        result
                    )

            elif channel_name == "BETTING":

                text = sball_templates.betting_sball_pass(
                    target_session["ball"],
                    result
                )

            elif channel_name == "BATMAN":

                text = sball_templates.batman_sball_pass(
                    target_session["ball"],
                    result
                )

            elif channel_name == "GAME":

                text = sball_templates.game_sball_pass(
                    target_session["ball"],
                    result
                )

            elif channel_name == "GUDDU":

                text = sball_templates.guddu_sball_pass(
                    target_session["ball"],
                    result
                )

            elif channel_name == "ROCKY":

                text = sball_templates.rocky_sball_pass(
                    target_session["ball"],
                    result
                )

            elif channel_name == "PRIYANSHU":

                text = sball_templates.priyanshu_sball_pass(
                    target_session["ball"],
                    result
                )

            elif channel_name == "JACKY":

                text = sball_templates.jacky_sball_pass(
                    target_session["ball"],
                    result
                )

            elif channel_name == "KING":

                text = sball_templates.king_sball_pass(
                    target_session["ball"],
                    result
                )

            elif channel_name == "ANGAD":

                text = sball_templates.angad_sball_pass(
                    target_session["ball"],
                    result
                )

            elif channel_name == "RAHUL":

                text = sball_templates.rahul_sball_pass(
                    target_session["ball"],
                    result
                )

            elif channel_name == "SHIVA":

                text = sball_templates.shiva_sball_pass(
                    target_session["ball"],
                    result
                )

            elif channel_name == "REDDY":

                text = sball_templates.reddy_sball_pass(
                    target_session["ball"],
                    result
                )

            elif channel_name == "TOSSKING":

                text = sball_templates.tossking_sball_pass(
                    target_session["ball"],
                    result
                )

            elif channel_name == "VIKRAM":

                text = sball_templates.vikram_sball_pass(
                    target_session["ball"],
                    result
                )

            elif channel_name == "PAWAN":

                text = sball_templates.pawan_sball_pass(
                    target_session["ball"],
                    result
                )

            elif channel_name == "DUBAI":

                text = sball_templates.dubai_sball_pass(
                    target_session["ball"],
                    result
                )

            elif channel_name == "SHUBHAM":

                text = sball_templates.shubham_sball_pass(
                    target_session["ball"],
                    result
                )

            elif channel_name == "VIKAS":

                text = sball_templates.vikas_sball_pass(
                    target_session["ball"],
                    result
                )

            elif channel_name == "FIXER":

                text = sball_templates.fixer_sball_pass(
                    target_session["ball"],
                    result
                )

            else:

                continue

            await send_text_safe(
                client,
                channel,
                text,
                msg_id,
                channel_name
            )

        target_session["status"] = "passed"

        save_memory(data)

        await event.reply(
            "✅ BALL SESSION PASS POSTED"
        )


print("✅ SBALL PASS HANDLER LOADED")