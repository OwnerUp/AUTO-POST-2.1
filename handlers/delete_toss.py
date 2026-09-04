# =========================================
# handlers/delete_toss.py
# =========================================

from telethon import events

from memory.memory_manager import *


def register_delete_toss_handler(client):

    @client.on(events.NewMessage(pattern=r'^/dtoss$|^/dtoss\s+\d+$'))

    async def delete_toss_handler(event):

        cmd = event.raw_text.split()

        if len(cmd) != 2:

            await event.reply(
                "USE:\n/dtoss 1"
            )

            return

        try:
            toss_id = int(cmd[1])

        except ValueError:

            await event.reply(
                "❌ INVALID TOSS ID"
            )

            return

        data = load_memory()

        selected = None

        for toss in data["tosses"]:

            if toss["id"] == toss_id:

                selected = toss

                break

        if not selected:

            await event.reply(
                "❌ TOSS ID NOT FOUND"
            )

            return

        if selected.get("status") == "deleted":

            await event.reply(
                "❌ TOSS ALREADY DELETED"
            )

            return

        # =====================================
        # DELETE FROM ALL CHANNELS
        # =====================================

        for post in selected["posts"]:

            channel = post["channel_id"]

            messages = []

            if post.get("photo_id"):
                messages.append(post["photo_id"])

            if post.get("promo_id"):
                messages.append(post["promo_id"])

            if messages:

                try:

                    await client.delete_messages(
                        channel,
                        messages
                    )

                except Exception as e:

                    print(f"DELETE ERROR : {e}")

        # =====================================
        # SAVE STATUS
        # =====================================

        selected["status"] = "deleted"

        save_memory(data)

        await event.reply(
            f"✅ TOSS DELETED\n🆔 ID : {toss_id}"
        )


print("✅ DELETE TOSS HANDLER LOADED")