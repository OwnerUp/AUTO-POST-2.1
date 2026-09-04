from telethon import events
import re

from memory.memory_manager import load_memory, save_memory
from utils import send_media_safe
from dynamic_render import render as render_dynamic
from templates.cashout_templates import get_cashout_template

print("✅ CASHOUT HANDLER LOADED")


def register_cashout_handler(client):

    @client.on(events.NewMessage(pattern=r'^/cashout'))
    async def cashout_handler(event):

        me = await client.get_me()

        if event.chat_id != me.id:
            return

        reply_msg = await event.get_reply_message()

        if not reply_msg or not reply_msg.media:
            await event.reply(
                "❌ Cash Out Photo ko reply karke /cashout bhejo."
            )
            return

        text = event.raw_text.strip()

        pattern = r"/cashout\s*entry:\s*(\d+)"

        m = re.search(pattern, text, re.I)

        if not m:
            await event.reply(
                "❌ Format:\n\n"
                "/cashout\n\n"
                "entry: 1"
            )
            return

        entry_id = int(m.group(1))

        memory = load_memory()

        entry_data = None

        for item in memory.get("entries", []):
            if item["id"] == entry_id:
                entry_data = item
                break

        if not entry_data:
            await event.reply(f"❌ Entry ID {entry_id} Not Found")
            return

        match_id = entry_data["match_id"]

        match_data = None

        for item in memory.get("matches", []):
            if item["id"] == match_id:
                match_data = item
                break

        if not match_data:
            await event.reply("❌ Match Not Found")
            return

        if "posts" not in match_data:
            await event.reply("❌ Match Posts Not Found")
            return

        success = 0
        failed = 0

        print("=" * 60)
        for post in match_data["posts"]:

            try:

                print(f"➡ Sending : {post['channel_name']}")

                dyn = render_dynamic(post["channel_name"], "cashout", {
                    "ENTRY": entry_id,
                    "CALL": entry_data.get("call", ""),
                    "RATE": entry_data.get("rate", ""),
                    "FAV": entry_data.get("fav", ""),
                    "LIMIT": entry_data.get("limit", ""),
                    "KHAO": entry_data.get("khao", ""),
                    "WIN": entry_data.get("win", "")
                })
                caption, template_entities = dyn if dyn else (get_cashout_template(post["channel_name"]), [])

                reply_id = post.get(
                    "entry_photo_id",
                    post.get("photo_id", post.get("msg_id"))
                )

                sent = await send_media_safe(
                    client=client,
                    channel=post["channel_id"],
                    reply_msg=reply_msg,
                    caption=caption,
                    channel_name=post["channel_name"],
                    reply_to=reply_id,
                    template_entities=template_entities
                )

                if sent:
                    post["cashout_photo_id"] = sent.id

                print(f"✅ Success : {post['channel_name']}")

                success += 1

            except Exception as e:

                print(f"❌ Failed : {post['channel_name']}")
                print(e)

                failed += 1

        print("=" * 60)

        save_memory(memory)

        await event.reply(
            f"✅ CASH OUT COMPLETED\n\n"
            f"Success : {success}\n"
            f"Failed : {failed}"
        )