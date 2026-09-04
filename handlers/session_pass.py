# =========================================
# handlers/session_pass.py
# =========================================

from telethon import events

from memory.memory_manager import *

from templates.session_templates import *

from utils import send_text_safe
from dynamic_render import render as render_dynamic

def register_session_pass_handler(client):

    @client.on(events.NewMessage(pattern='/spass'))

    async def session_pass_handler(event):

        me = await client.get_me()

        if event.chat_id != me.id:
            return

        raw = event.raw_text.replace(
            '/spass',
            ''
        ).strip()

        parts = raw.split()

        if len(parts) != 2:

            await event.reply(
                "USE:\n/spass 1 84"
            )

            return

        session_id = int(parts[0])

        result = parts[1]

        data = load_memory()

        target_session = None

        for session in data["sessions"]:
            if session["id"] == session_id:
                if session["status"] == "passed":
                    await event.reply(
                        "❌ SESSION ALREADY PASSED"
                    )
                    return

                target_session = session
                break

        if not target_session:
            await event.reply(
                "SESSION ID NOT FOUND"
            )
            return

        for post in target_session["posts"]:
            channel = post["channel_id"]
            msg_id = post["msg_id"]
            channel_name = post["channel_name"]

            dyn = render_dynamic(channel_name, "session_pass", {"OVER": target_session["over"], "RESULT": result})
            if dyn:
                text, template_entities = dyn
                await send_text_safe(client, channel, text, msg_id, channel_name, template_entities=template_entities)
                continue

            if channel_name == "ROYAL":
                text = royal_session_pass(
                    target_session["over"],
                    result
                )
            elif channel_name == "BETTING":
                text = betting_session_pass(
                    result
                )
            elif channel_name == "BATMAN":
                text = batman_session_pass(
                    result
                )
            elif channel_name == "GAME":
                text = game_session_pass(
                    result
                )
            elif channel_name == "GUDDU":
                text = guddu_session_pass(
                    result
                )
            elif channel_name == "ROCKY":
                text = rocky_session_pass(
                    result
                )
            elif channel_name == "PRIYANSHU":
                text = priyanshu_session_pass(
                    result
                )
            elif channel_name == "JACKY":
                text = jacky_session_pass(
                    result
                )
            elif channel_name == "KING":
                text = king_session_pass(
                    result
                )
            elif channel_name == "ANGAD":
                text = angad_session_pass(
                    result
                )
            elif channel_name == "RAHUL":
                text = rahul_session_pass(
                    result
                )
            elif channel_name == "SHIVA":
                text = shiva_session_pass(
                    result
                )
            elif channel_name == "REDDY":
                text = reddy_session_pass(
                    result
                )
            elif channel_name == "TOSSKING":
                text = tossking_session_pass(
                    result
                )
            else:
                text = batman_session_pass(
                    result
                )

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
            "✅ SESSION PASS POSTED"
        )


print("✅ SESSION PASS HANDLER LOADED")