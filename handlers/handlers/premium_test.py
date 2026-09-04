# =========================================
# handlers/premium_test.py
# =========================================

from telethon import events
from telethon.tl.types import MessageEntityCustomEmoji


# =========================================
# REGISTER
# =========================================

def register_premium_test(client):

    @client.on(events.NewMessage(pattern='/ptest'))

    async def premium_test(event):

        if not event.message.entities:

            await event.reply(
                "NO PREMIUM EMOJI FOUND"
            )
            return

        premium_emoji = None

        for entity in event.message.entities:

            if isinstance(entity, MessageEntityCustomEmoji):

                premium_emoji = entity
                break

        if not premium_emoji:

            await event.reply(
                "SEND PREMIUM EMOJI"
            )
            return

        text = "TEST ❤️ PREMIUM"

        heart_index = text.find("❤️")

        entities = [

            MessageEntityCustomEmoji(

                offset=heart_index,

                length=2,

                document_id=premium_emoji.document_id

            )

        ]

        await client.send_message(

            event.chat_id,

            text,

            formatting_entities=entities

        )

        await event.reply(
            "✅ PREMIUM TEST DONE"
        )


print("✅ PREMIUM TEST LOADED")