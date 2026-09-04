
from telethon import events
import re
from dynamic_emoji import get_text_custom_emojis
from dynamic_render import render as render_dynamic

from templates.entry_templates import get_entry_template
from memory.memory_manager import load_memory, save_memory
from utils import send_media_safe

print("✅ ENTRY HANDLER LOADED")


def register_entry_handler(client):

    @client.on(events.NewMessage(pattern=r'^/entry'))
    async def entry_handler(event):

        me = await client.get_me()

        if event.chat_id != me.id:
            return

        reply_msg = await event.get_reply_message()

        if not reply_msg or not reply_msg.media:
            await event.reply("❌ Entry Photo ko reply karke /entry bhejo.")
            return

        text = event.raw_text.strip()

        pattern = (
            r"/entry\s*"
            r"match:\s*(\d+)\s*"
            r"call:\s*(.*?)\s*"
            r"rate:\s*(.*?)\s*"
            r"fav:\s*(.*?)\s*"
            r"limit:\s*(.*?)\s*"
            r"khao:\s*(.*?)\s*"
            r"win:\s*(.+)"
        )

        m = re.search(pattern, text, re.S | re.I)

        if not m:
            await event.reply(
                "❌ Format:\n\n"
                "/entry\n\n"
                "match: 1\n"
                "call: 1ST\n"
                "rate: 58-59\n"
                "fav: BIRMINGHAM PHOENIX\n"
                "limit: 40%\n"
                "khao: BIRMINGHAM PHOENIX\n"
                "win: BIRMINGHAM PHOENIX"
            )
            return

        match_id = int(m.group(1))

        memory = load_memory()

        match_data = None

        for item in memory.get("matches", []):
            if item["id"] == match_id:
                match_data = item
                break

        if not match_data:
            await event.reply(f"❌ Match ID {match_id} Not Found")
            return

        if "posts" not in match_data:
            await event.reply(
                "❌ Is Match me Posts Save nahi hain.\n\n"
                "Naya /match bana kar phir /entry bhejo."
            )
            return

        call = m.group(2).strip().upper()
        rate = m.group(3).strip()
        fav = m.group(4).strip()
        limit = m.group(5).strip()
        khao = m.group(6).strip()
        win = m.group(7).strip()
        fav_custom_emojis = get_text_custom_emojis(
            event,
            fav
        )

        khao_custom_emojis = get_text_custom_emojis(
            event,
            khao,
            occurrence=2
        )

        win_custom_emojis = get_text_custom_emojis(
            event,
            win
        )

        dynamic_items = [
            {
                "text": fav,
                "emojis": fav_custom_emojis
            },
            {
                "text": khao,
                "emojis": khao_custom_emojis
            },
            {
                "text": win,
                "emojis": win_custom_emojis
            }
        ]

        memory.setdefault("entries", [])

        entry_id = len(memory["entries"]) + 1

        memory["entries"].append({
            "id": entry_id,
            "match_id": match_id,
            "call": call,
            "rate": rate,
            "fav": fav,
            "limit": limit,
            "khao": khao,
            "win": win,
            "status": "ACTIVE"
        })

        save_memory(memory)

        success = 0
        failed = 0

        print("=" * 60)

        for post in match_data["posts"]:

            try:

                print(f"➡ Sending : {post['channel_name']}")

                dyn = render_dynamic(post["channel_name"], "entry", {"CALL": call, "RATE": rate, "FAV": fav, "LIMIT": limit, "KHAO": khao, "WIN": win})
                if dyn:
                    caption, template_entities = dyn
                    reply_id = post.get("photo_id", post.get("msg_id"))
                    sent = await send_media_safe(client=client, channel=post["channel_id"], reply_msg=reply_msg, caption=caption, channel_name=post["channel_name"], dynamic_items=dynamic_items, reply_to=reply_id, template_entities=template_entities)
                    if sent:
                        post["entry_photo_id"] = sent.id
                    success += 1
                    continue

                caption = get_entry_template(
                    post["channel_name"],
                    call,
                    rate,
                    fav,
                    limit,
                    khao,
                    win
                )

                reply_id = post.get("photo_id", post.get("msg_id"))
                
                sent = await send_media_safe(
                client=client,
                channel=post["channel_id"],
                reply_msg=reply_msg,
                caption=caption,
                channel_name=post["channel_name"],
                dynamic_items=dynamic_items,
                reply_to=reply_id
            )

                if sent:
                    post["entry_photo_id"] = sent.id

                print(f"✅ Success : {post['channel_name']}")
                success += 1

            except Exception as e:

                print(f"❌ Failed : {post['channel_name']}")
                print(e)

                failed += 1

        print("=" * 60)

        save_memory(memory)

        await event.reply(
            f"✅ ENTRY COMPLETED\n\n"
            f"Success : {success}\n"
            f"Failed : {failed}\n\n"
            f"Entry ID : {entry_id}"
        )