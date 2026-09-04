# =========================================
# handlers/sball_loss.py
# =========================================

from telethon import events

from memory.memory_manager import *

from templates.sball_templates import *

from utils import send_text_safe
from dynamic_render import render as render_dynamic

def register_sball_loss_handler(client):

    @client.on(events.NewMessage(pattern='/sbloss'))

    async def sbloss_handler(event):

        me = await client.get_me()

        if event.chat_id != me.id:
             return

        raw = event.raw_text.replace(
            '/sbloss',
            ''
        ).strip()

        if not raw:

            await event.reply(
                "USE:\n/sbloss 1"
            )

            return

        sball_id = int(raw)

        data = load_memory()

        target_sball = None

        for sball in data["sballs"]:

            if sball["id"] == sball_id:

                if sball["status"] == "loss":

                    await event.reply(
                        "❌ BALL SESSION ALREADY LOSS"
                    )

                    return

                target_sball = sball

                break

        if not target_sball:

            await event.reply(
                "BALL SESSION ID NOT FOUND"
            )

            return

        for post in target_sball["posts"]:

            channel = post["channel_id"]

            msg_id = post["msg_id"]

            channel_name = post["channel_name"]

            dyn = render_dynamic(channel_name, "sball_loss", {})
            if dyn:
                text, template_entities = dyn
                await send_text_safe(client, channel, text, msg_id, channel_name, template_entities=template_entities)
                continue

            if channel_name == "ROYAL":

                text = royal_sball_loss()

            elif channel_name == "BETTING":

                text = betting_sball_loss()

            elif channel_name == "BATMAN":

                text = batman_sball_loss()

            elif channel_name == "GAME":

                text = game_sball_loss()

            elif channel_name == "GUDDU":

                text = guddu_sball_loss()

            elif channel_name == "ROCKY":

                text = rocky_sball_loss()

            elif channel_name == "PRIYANSHU":

                text = priyanshu_sball_loss()

            elif channel_name == "JACKY":

                text = jacky_sball_loss()

            elif channel_name == "KING":

                text = king_sball_loss()

            elif channel_name == "ANGAD":

                text = angad_sball_loss()

            elif channel_name == "RAHUL":

                text = rahul_sball_loss()

            elif channel_name == "SHIVA":

                text = shiva_sball_loss()

            elif channel_name == "REDDY":

                text = reddy_sball_loss()

            elif channel_name == "TOSSKING":

                text = tossking_sball_loss()

            elif channel_name == "VIKRAM":

                text = vikram_sball_loss()

            elif channel_name == "PAWAN":

                text = pawan_sball_loss()

            elif channel_name == "DUBAI":

                text = dubai_sball_loss()

            elif channel_name == "SHUBHAM":

                text = shubham_sball_loss()

            elif channel_name == "VIKAS":

                text = vikas_sball_loss()

            elif channel_name == "FIXER":

                text = fixer_sball_loss()

            else:

                text = batman_sball_loss()

            await send_text_safe(
                client,
                channel,
                text,
                msg_id,
                channel_name
            )

            target_sball["status"] = "loss"

        save_memory(data)

        await event.reply(
        "✅ BALL SESSION LOSS POSTED"
            )

print("✅ SBALL LOSS HANDLER LOADED")
