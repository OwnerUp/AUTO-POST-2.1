# =========================================
# handlers/match_pass.py
# FINAL FULLY FIXED WORKING VERSION
# =========================================

import re
from unittest import result

from telethon import events

from dynamic_emoji import get_text_custom_emojis

from utils import send_text_safe

from handlers.match_handler import match_posts

from memory.memory_manager import *
from dynamic_render import render as render_dynamic


# =========================================
# REGISTER
# =========================================

def register_match_pass_handler(client):

    @client.on(events.NewMessage(pattern=r'^/mpass'))

    async def match_pass_handler(event):

        me = await client.get_me()

        if event.chat_id != me.id:
            return

        print("MATCH PASS HIT")
        print(event.raw_text)

        raw = event.raw_text.strip()

# =========================================
# FORMAT:
# /mpass 1 (TEAM NAME) WON BY (RESULT)
# =========================================

        m = re.match(
         r'^/mpass\s+(\d+)\s+\((.*?)\)\s+WON\s+BY\s+\((.*?)\)$',
        raw,
        re.IGNORECASE
        )

        if not m:
            await event.reply(
                "❌ WRONG FORMAT\n\nUSE:\n/mpass 1 (INDIA WOMEN) WON BY (10 WICKETS)"
            )
            return

        match_id = int(m.group(1))
        team = m.group(2).strip().upper()
        result = m.group(3).strip().upper()

        team_custom_emojis = get_text_custom_emojis(
            event,
            team,
            occurrence=1
        )

        print(
            "🔥 MPASS TEAM EMOJIS:",
            team_custom_emojis
        )

        result_custom_emojis = get_text_custom_emojis(
            event,
            result,
            occurrence=1
        )

        print(
            "🔥 MPASS RESULT EMOJIS:",
            result_custom_emojis
        )
        
        
        data = load_memory()

        selected = None

        for match in data["matches"]:
            if match["id"] == match_id:
                if match["status"] == "passed":
                    await event.reply(
                        "❌ MATCH ALREADY PASSED"
                    )
                    return

                selected = match["posts"]
                break

        if not selected:
            await event.reply(
                "MATCH ID NOT FOUND"
            )
            return

        # =====================================
        # LOOP
        # =====================================

        for post in selected:
                        
            channel = post["channel_id"]

            msg_id = post["photo_id"]
        
            channel_name = post["channel_name"]

            ctype = channel_name

            dyn = render_dynamic(channel_name, "match_pass", {"TEAM": team, "RESULT": result})
            if dyn:
                text, template_entities = dyn
                await send_text_safe(client, channel, text, msg_id, channel_name, dynamic_items=[{"text": team, "emojis": team_custom_emojis}, {"text": result, "emojis": result_custom_emojis}], template_entities=template_entities)
                continue

            # =====================================
            # ROYAL
            # =====================================

            if ctype == "ROYAL":

                text = f"""ROYALS WIN KE SATH ONLY PROFIT 🏆

{team} WIN BY {result} 🏆

🤜 B O O M B O O M 🤜

AGEN FUCK ALL MARKET 🤑

ROYALS WIN 💠"""

            # =====================================
            # BATMAN
            # =====================================

            elif ctype == "BATMAN":

                text = f"""AGEN FUCK ALL MARKET🥳

{team} WON BY {result} ✅

💥 Back to Back Pass 💥

🏆🏆Jeet Mubarak 🏆🏆

BATMAN (Official) 💠"""

            # =====================================
            # GAME
            # =====================================

            elif ctype == "GAME":

                text = f"""ONLY ON PROFIT 🏆

{team} WON BY {result} 🏆

🤜B O O M B O O M🤜

GAME CHANGER ABHI KE SATH

 ONLY ON PROFIT 🏆

AGEN FUCK ALL MARKET 🤑

GAME CHANGER ABHI 💠"""

            # =====================================
            # GUDDU
            # =====================================

            elif ctype == "GUDDU":

                text = f"""PASS MATCH ✅ PROFIT DONE 🏆

{team} won by {result}

ONLY ON PROFIT 🏆

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

Guddu Bhaiya ✅"""

            # =====================================
            # ROCKY
            # =====================================

            elif ctype == "ROCKY":

                text = f"""Back-to-Back Match PASS 💥🔥

{team} WIN BY {result} ✅

Market mein sirf naam hi nahi… kaam bhi bolta hai 💯

Poora market ek taraf…
Apka bhai Akele 😎👑

Kyon pade ho chakkaron mein?
Koi nahi hai takkar mein! 💪🔥

Rocky bhai (Trending King) 💠"""

            # =====================================
            # JACKY
            # =====================================

            elif ctype == "JACKY":

                text = f"""🔥 Another Successful Call 🔥

{team} WON BY {result} ✅

🎯 Exact Match Prediction Passed 💯

🔥 Another Successful Call 🔥

💵 Profit Done For Premium Members 💵

Only 🔻 JACKY FIXER 💠"""

            # =====================================
            # PRIYANSHU
            # =====================================

            elif ctype == "PRIYANSHU":

                text = f"""JACKPOT MATCH ✅ PROFIT DONE 🏆

{team} WIN BY {result}

🤜B O O M B O O M🤜

PRIYANSHU BHAI KE SATH ONLY PROFIT 🏆

SUPRE SURE MATCH
ONLY ONE IN MARKET
AGEN FUCK ALL MARKET 🤑

PRIYANSHU BHAI 💠"""

            # =====================================
            # TOSS KING
            # =====================================

            elif ctype == "TOSSKING":

                text = f"""Profit Done For Premium Members 💵
                
🏏 {team} WON BY {result} ✅️

Match Passed 💯

Another Successful Call 🔥

Profit Done For Premium Members 💵

CALL ➡️TOSS KING(Aditya)💠"""

            # =====================================
            # REDDY
            # =====================================

            elif ctype == "REDDY":

                text = f"""BACK TO BACK MATCH PASS ✅ PROFIT DONE 🏆

{team} WIN BY {result}

🤜B O O M B O O M🤜

SUPRE SURE MATCH
ONLY ONE IN MARKET
AGEN FUCK ALL MARKET 🤑

ANNA SAHAB 💠"""

            # =====================================
            # SHIVA
            # =====================================

            elif ctype == "SHIVA":

                text = f"""MARKET KA BOSS SHIVA 🔥

{team} WON BY {result}🏆

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

Happy for Win

✅ All Market Fail
✅ Bane raho aur profit karo.....

ONLY🔻SHIVA REDDY 💠"""

            # =====================================
            # RAHUL
            # =====================================

            elif ctype == "RAHUL":

                text = f"""JACKPOT KA BOSS RAHUL DADA 🔥

{team} WIN BY {result}

ONLY PROFIT 🏆

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

🏆🏆Jeet Mubarak 🏆🏆

✅ Boom Boom Boom…
✅ Full Market Fail…
✅ Always Profit With Me.....

ONLY ➡️ RAHUL DADA 💠"""

            # =====================================
            # ANGAD
            # =====================================

            elif ctype == "ANGAD":

                text = f"""🏆🏆Jeet Mubarak 🏆🏆

{team} WON BY {result} 🏆

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

✔️ Boom Boom Boom…
✔️ Full Market Fail…
✔️ Always Profit With Me.....

ONLY 🔻ANGAD DADA 💠"""

            # =====================================
            # KING
            # =====================================

            elif ctype == "KING":

                text = f"""AGEN FUCK ALL MARKET🥳

{team} WIN BY {result}

💥 Back to Back Pass 💥

ONLY PROFIT 🏆

AGEN FUCK ALL MARKET🥳

🏆🏆Jeet Mubarak 🏆🏆

✅ Boom Boom Boom…
✅ Full Market Fail…
✅ Always Profit With Me.....

𝐎𝐍𝐋𝐘 👉 KING BHAI 💠"""

             # =====================================
            # BETTING
            # =====================================

            elif ctype == "BETTING":

                text = f"""✅ Always Profit With Me.....

{team} WIN BY {result} 🏆

BETTING KING KE SATH ONLY PROFIT 🏆

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

🏆🏆Jeet Mubarak 🏆🏆
✅ Boom Boom Boom…
✅ Full Market Fail…

BK BHAI (BK) 💠"""

            # =====================================
            # VIKRAM
            # =====================================

            elif ctype == "VIKRAM":

                text = f"""JACKPOT MUBARAK HO SBHI KO 🏆

{team} WON BY {result} 🏆

💥 MATCH PASS 💥

🔥 BIG PROFIT DONE 🔥

🏆 PREMIUM MEMBERS WIN 🏆

OWNER 👉 VIKRAM SINGH 💠"""

            # =====================================
            # PAWAN
            # =====================================

            elif ctype == "PAWAN":

                text = f"""KING OF CRICKET MARKET 💠
JACKPOT PRIZE DONE 🏆

{team} WON BY {result} 🏆

💥 MATCH PASS 💥

🔥 BIG PROFIT DONE 🔥

🏆 PREMIUM MEMBERS WIN 🏆

OWNER 👉 PAWAN SINGH 💠"""

            # =====================================
            # DUBAI
            # =====================================

            elif ctype == "DUBAI":

                text = f"""KING OF CRICKET MARKET 💠

{team} WON BY {result} 🏆

💥 MATCH PASS 💥

🔥 BIG PROFIT DONE 🔥


🏆 PREMIUM MEMBERS WIN 🏆

OWNER 👉 RANA SAHAB 💠"""

           # =====================================
            # SHUBHAM
            # =====================================

            elif ctype == "SHUBHAM":

                text = f"""BACK TO BACK PASS  💠

{team} WON BY {result} 🏆

💥 MATCH PASS 💥

🔥 BIG PROFIT DONE 🔥

🏆 PREMIUM MEMBERS WIN 🏆

OWNER 👉 SHUBHAM PANDIT 💠"""

            # =====================================
            # VIKAS
            # =====================================

            elif ctype == "VIKAS":

                text = f"""

{team} WON BY {result} 🏆

💥 MATCH PASS 💥 🔥 BIG PROFIT DONE 🔥

🏆 PREMIUM MEMBERS WIN 🏆 ALL KHUS 

TO APNI JEET KA MAZA LO 🏆

OWNER 👉 VIKAS MUMBAI 💠"""

            # =====================================
            # FIXER
            # =====================================

            elif ctype == "FIXER":

                text = f"""APNI JEET KA MAZA LO SBHI 🏆

{team} WON BY {result} 🏆

💥THE JACKPOT MATCH PASS 💥

🔥 BIG PROFIT DONE 🔥

🏆 PREMIUM MEMBERS WIN 🏆

OWNER 👉 FIXER BHAI 💠"""     


            # =====================================
            # SEND
            # =====================================

            dynamic_items = [
                {
                    "text": team,
                    "emojis": team_custom_emojis
                },
                {
                    "text": result,
                    "emojis": result_custom_emojis
                }
            ]

            await send_text_safe(
                client,
                channel,
                text,
                msg_id,
                channel_name,
                dynamic_items=dynamic_items
            )

        # =====================================
        # MARK MATCH PASSED
        # =====================================

        for match in data["matches"]:

            if match["id"] == match_id:

                match["status"] = "passed"

                break

        save_memory(data)

        await event.reply(
            "✅ MATCH PASS POSTED"
        )

print("✅ MATCH PASS HANDLER LOADED")