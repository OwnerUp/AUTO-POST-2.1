# =========================================
# handlers/league_handler.py
# =========================================

from telethon import events

import config


# =========================================
# LEAGUE CHANGE
# =========================================

def register_league_handler(client):

    @client.on(events.NewMessage(pattern='/league'))

    async def league_handler(event):

        text = event.raw_text.replace(

            '/league',
            ''

        ).strip()

        if not text:

            await event.reply(

                "USE:\n/league IPL 2026"
            )

            return

        config.CURRENT_LEAGUE = text.upper()

        await event.reply(

            f"✅ LEAGUE CHANGED:\n\n{config.CURRENT_LEAGUE}"
        )


print("✅ LEAGUE HANDLER LOADED")