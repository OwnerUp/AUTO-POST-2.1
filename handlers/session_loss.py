# =========================================
# handlers/session_loss.py
# =========================================

from telethon import events

from memory.memory_manager import *

from templates.session_templates import *

from utils import send_text_safe
from dynamic_render import render as render_dynamic

def register_session_loss_handler(client):

    @client.on(events.NewMessage(pattern='/sloss'))

    async def session_loss_handler(event):

        me = await client.get_me()

        if event.chat_id != me.id:
             return

        raw = event.raw_text.replace(
            '/sloss',
            ''
        ).strip()

        if not raw:

            await event.reply(
                "USE:\n/sloss 1"
            )

            return

        session_id = int(raw)

        data = load_memory()

        target_session = None

        for session in data["sessions"]:

            if session["id"] == session_id:

                if session["status"] == "loss":

                    await event.reply(
                        "❌ SESSION ALREADY LOSS"
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

            dyn = render_dynamic(channel_name, "session_loss", {})
            if dyn:
                text, template_entities = dyn
                await send_text_safe(client, channel, text, msg_id, channel_name, template_entities=template_entities)
                continue

            if channel_name == "ROYAL":

                text = royal_session_loss()

            elif channel_name == "BETTING":

                text = betting_session_loss()

            elif channel_name == "BATMAN":

                text = batman_session_loss()

            elif channel_name == "GAME":

                text = game_session_loss()

            elif channel_name == "GUDDU":

                text = guddu_session_loss()

            elif channel_name == "ROCKY":

                text = rocky_session_loss()

            elif channel_name == "PRIYANSHU":

                text = priyanshu_session_loss()

            elif channel_name == "JACKY":

                text = jacky_session_loss()

            elif channel_name == "KING":

                text = king_session_loss()

            elif channel_name == "ANGAD":

                text = angad_session_loss()

            elif channel_name == "RAHUL":

                text = rahul_session_loss()

            elif channel_name == "SHIVA":

                text = shiva_session_loss()

            elif channel_name == "REDDY":

                text = reddy_session_loss()

            elif channel_name == "TOSSKING":

                text = tossking_session_loss()

            else:

                text = batman_session_loss()

            await send_text_safe(
                client,
                channel,
                text,
                msg_id,
                channel_name
            )

            target_session["status"] = "loss"

        save_memory(data)

        await event.reply(
        "✅ SESSION LOSS POSTED"
            )

print("✅ SESSION LOSS HANDLER LOADED")