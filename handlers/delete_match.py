# =========================================
# handlers/delete_match.py
# =========================================

from telethon import events

from memory.memory_manager import *


def register_delete_match_handler(client):

    @client.on(events.NewMessage(pattern=r'^/dmatch$|^/dmatch\s+\d+$'))
    async def delete_match_handler(event):

        me = await client.get_me()

        if event.chat_id != me.id:
            return

        cmd = event.raw_text.split()

        if len(cmd) != 2:

            await event.reply(
                "USE:\n/dmatch 1"
            )
            return

        try:
            match_id = int(cmd[1])

        except ValueError:

            await event.reply(
                "❌ INVALID MATCH ID"
            )
            return

        data = load_memory()

        selected = None

        for match in data["matches"]:

            if match["id"] == match_id:

                selected = match
                break

        if not selected:

            await event.reply(
                "❌ MATCH ID NOT FOUND"
            )
            return

        if selected.get("status") == "deleted":

            await event.reply(
                "❌ MATCH ALREADY DELETED"
            )
            return

        # =====================================
        # DELETE FROM ALL CHANNELS
        # =====================================

        for post in selected["posts"]:

            channel = post["channel_id"]

            messages = []

            # Photo
            if post.get("photo_id"):
                messages.append(post["photo_id"])

            # Promo 1
            if post.get("promo1_id"):
                messages.append(post["promo1_id"])

            # Promo 2
            if post.get("promo2_id"):
                messages.append(post["promo2_id"])

            print("CHANNEL :", channel)
            print("MESSAGES :", messages)

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
            f"✅ MATCH DELETED\n🆔 ID : {match_id}"
        )


print("✅ DELETE MATCH HANDLER LOADED")