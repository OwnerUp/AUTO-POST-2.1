# =========================================
# templates/session_templates.py
# =========================================


def session_call_emoji(call):
    if call == "YES":
        return "✅"
    return "❌"


# =========================================
# ROYAL
# =========================================

def royal_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
{over} OVER 🌐 {call} KARO {emoji}

{run} RUN 🏏

Play Only Trusted Sites 👇

Plat at -- Www.Khelking.buzz


""".strip()


def royal_session_pass(over, result):

    return f"""{over} OVER 👑

{result} 🅿️🅰️💲💲✔️

SESSIONS PASS 💸❤️
""".strip()


def royal_session_loss():

    return """
LOSS RAHA APNA DONT WORRY ❤️

WAIT FOR NEXT ❌
""".strip()


# =========================================
# BETTING
# =========================================

def betting_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
{run} RUN 👍 {over} OVER 🏏

{call} KARO {emoji}

 JACKPOT PLAY 👇

10K LIMIT SE PLAY 🥳
""".strip()


def betting_session_pass(result):

    return f"""
{result} 🅿️🅰️💲💲✔️✔️

SESSIONS PASS 💰🔥

💫 🅱𝗢𝗢Ⓜ️ 💫 🅱𝗢𝗢Ⓜ
""".strip()


def betting_session_loss():

    return """
SESSION LOSS ❌
""".strip()


# =========================================
# BATMAN
# =========================================

def batman_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""BINDASS 👍
    
{over} OVER 👉 {run} RUN

{call} KARO 👉 {emoji}

SAME LIMIT SE PLAY 💰
""".strip()


def batman_session_pass(result):

    return f"""
{result} 🅿️🅰️💲💲 🤑🤑

🤑 SESSIONS PASS 💰
""".strip()


def batman_session_loss():

    return """
SESSION LOSS 😒
""".strip()


# =========================================
# GAME
# =========================================

def game_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
 {call} KARO {emoji}

{over} OVER 🏏 {run} RUN 

INIDAN TRUSTED SITE 👇

Www.Khelking.buzz 💯

""".strip()


def game_session_pass(result):

    return f"""🔥 TARGET HIT 🔥

SESSIONS PASS 💸

{result} 🅿️🅰️💲💲
""".strip()


def game_session_loss():

    return """
LOSS ❌ KOI BAAT NHI 

NEXT SESSION 💯 COVER HOGA 👍
""".strip()


# =========================================
# GUDDU
# =========================================

def guddu_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""

SESSION UPDATE 📊 

{run} RUN 🎯 {over}  OVER 🏏

{call} KARO {emoji}

10K LIMIT SE PLAY 💰
""".strip()


def guddu_session_pass(result):

    return f"""
 💸 SESSIONS PASS 💸

{result} 🅿️🅰️💲💲✔️✔️

🏆 SESSION PASSED

📊 RESULT ➜ {result}

💰 PROFIT BOOKED
""".strip()


def guddu_session_loss():

    return """
 SESSION MISSED 😒

KEEP PATIENCE
NEXT ONE WILL COVER IT 💯
""".strip()


# =========================================
# ROCKY
# =========================================

def rocky_session(over, run, call):
    emoji = session_call_emoji(call)

    
    return f"""
 👇 LIVE SESSION 👇

{run} RUN 👉 {over} OVER

{call} KRO {emoji}

""".strip()


def rocky_session_pass(result):

    return f"""
🅿️🅰️💲💲🏆🏆

🏏 RESULT 👉 {result}

🏆 BACK TO BACK PASS 🏆
""".strip()

def rocky_session_loss():

    return """
SESSION LOSS ❌

NEXT SESSION PASS ROCKY PROMISE
""".strip()


# =========================================
# PRIYANSHU
# =========================================

def priyanshu_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
🌐 LIVE UPDATE 🌐

{run} RUN 👉 {over} OVER 🏏

{call} KRO SAB {emoji}
""".strip()


def priyanshu_session_pass(result):

    return f"""
 {result} 🅿️🅰️💲💲🏆

💰 WINNING SESSION 💰

 WAIT FOR NEXT SESSION 💯
""".strip()

def priyanshu_session_loss():

    return """
❌ SESSION LOSS 😊 DON'T WORRY

NEXT SESSION WILL PASS 🎯 

WAIT FOR NEXT SESSION 💯
""".strip()


# =========================================
# JACKY
# =========================================

def jacky_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
PLAY WHIT SAME LIMIT ✔️

🏏 {run} RUN 🔻 {over} OVER

 {call} KRO {emoji}

""".strip()


def jacky_session_pass(result):

    return f"""
{result} RUN SESSION 🅿🅰🆂🆂 

🔻SESSIONS PASS 🔻

💣 BOOM 💣 BOOM 💣
""".strip()


def jacky_session_loss():

    return """
SESSION WILL BE LOSS❌
""".strip()


# =========================================
# KING
# =========================================

def king_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
🔻 SESSION LIVE 🔻

{run} RUN 👉 {over} OVER

{call} KARO SAB {emoji}

PLAY ON SAME LIMIT 💰

""".strip()


def king_session_pass(result):

    return f"""💣 BOOM 💣 🔻 💣 BOOM 💣

{result} RUN 🅿️🅰️💲💲

🤑 SESSIONS PASS 🤑

👑 KING ENTRY 👑
""".strip()


def king_session_loss():

    return """

😒 SESSION LOSS 😒 KEEP TRUST

🎯 NEXT SESSION WILL PASS 🎯

""".strip()


# =========================================
# ANGAD
# =========================================

def angad_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
💠 DADA ENTRY 💠

{call} KRO SAB {emoji}

{over} OVER ME 🏏 {run} RUN
""".strip()


def angad_session_pass(result):

    return f"""
🏏 {result} RUN

💯 🅿🅰🆂🆂 💯

🏏 {result} RUN

ANGAD DADA 💠
""".strip()


def angad_session_loss():

    return """
❌ 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 𝗟𝗢𝗦𝗦

🎯 NEXT CALL WILL BE BETTER
""".strip()


# =========================================
# RAHUL
# =========================================

def rahul_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
SESSION PASS 1000% BINDAS PLAY KRO

{run} RUN 👉 {call} KARO {emoji}

{over} OVER 🏏

""".strip()


def rahul_session_pass(result):

    return f"""
💯 SESSIONS PASS 💯

{result} RUN 🅿️🅰️💲💲

ACCURATE ENTRY 💯

RAHUL DADA 💠
""".strip()


def rahul_session_loss():

    return """
🔻 SESSION LOSS 🔻

 DON'T LOSE TRUST 👍
""".strip()


# =========================================
# SHIVA
# =========================================

def shiva_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
🔥 SHIVA REDDY  🔥

{over} OVER 👉 {run} RUN

{call} KARO SAB {emoji}

FULL SUPPORT ❤️
""".strip()


def shiva_session_pass(result):

    return f"""
{result} RUN 🔥 SHIVA REDDY

💯 🅿🅰🆂🆂 💯

🏏 {result} RUN

👑 PERFECT CALL
""".strip()


def shiva_session_loss():

    return """
💠 RAHUL DADA

❌ 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 𝗟𝗢𝗦𝗦

🎯 NEXT CALL WILL BE BETTER
""".strip()

# =========================================
# REDDY
# =========================================

def reddy_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
ACTIVE ALL MEMBERS 🔔

 {run} RUN 🔻 {over} OVER

{call} KRO FATA FAT {emoji}

PALY WITH SAME LIMIT 💰
""".strip()


def reddy_session_pass(result):

    return f"""
{result} RUN SESSION 🅿️🅰️💲💲

 🔻 SESSIONS PASS 🔻
💯 BACK TO BACK PASS 💯

ONLY 👉 REDDY ANNA 💠
""".strip()


def reddy_session_loss():

    return """
SESSION LOSS 😒

🎯 NEXT CALL SOON
""".strip()


# =========================================
# TOSSKING
# =========================================

def tossking_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""
🌐 SESSION 🌐

🏏 {run} RUN 🔻 {over} OVER

 {call} KRO {emoji}

WAIT FOR NEXT SESSION 💯
""".strip()


def tossking_session_pass(result):

    return f"""
💯🅿🅰🆂🆂💯

🏏 {result} RUN

🔥 KING PERFECT CALL
""".strip()


def tossking_session_loss():

    return """
⚠️ 🅻🅾🆂🆂 ⚠️

💎 TRUST THE PROCESS
""".strip()

# =========================================
# VIKRAM
# =========================================

def vikram_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""PLAY SAME LIMIT 💰

{run} RUN 👉 {over} OVER

{call} KARO {emoji}

🏏 VIKRAM SINGH 💠
""".strip()


def vikram_session_pass(result):

    return f"""MUBARAK HO SESSIONS PASS 💯

🏏 {result} RUN

🅿️🅰️💲💲✔️

OWNER 👉 VIKRAM SINGH 💠
""".strip()


def vikram_session_loss():

    return """
❌ SESSION LOSS

DON'T WORRY ❤️

NEXT SESSION COVER 💯

OWNER 👉 VIKRAM SINGH 💠
""".strip()

# =========================================
# PAWAN
# =========================================

def pawan_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""🏏 PAWAN SINGH 💠

{run} RUN 👉 {over} OVER

{call} KARO {emoji}

PLAY SAME LIMIT 💰
""".strip()


def pawan_session_pass(result):

    return f"""KING OF MARKET 💠

🏏 {result} RUN

🅿️🅰️💲💲✔️

OWNER 👉 PAWAN SINGH 💠
""".strip()


def pawan_session_loss():

    return """
❌ SESSION LOSS

DON'T WORRY ❤️

NEXT SESSION COVER 💯

OWNER 👉 PAWAN SINGH 💠
""".strip()

# =========================================
# DUBAI
# =========================================

def dubai_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""JACKPOT 💯 SESSION 💯

{run} RUN 👉 {over} OVER

{call} KARO {emoji}

PLAY SAME LIMIT 💰
""".strip()


def dubai_session_pass(result):

    return f"""BOOM 💣 BOOM 💣 BOOM 💣

🏏 {result} RUN

🅿️🅰️💲💲✔️
""".strip()


def dubai_session_loss():

    return """
❌ SESSION LOSS

DON'T WORRY ❤️

NEXT SESSION COVER 💯
""".strip()

# =========================================
# SHUBHAM
# =========================================

def shubham_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""BINDASS PLAY KRO SBHI 💯

{run} RUN 👉 {over} OVER

{call} KARO {emoji}

PLAY SAME LIMIT 💰
""".strip()


def shubham_session_pass(result):

    return f"""JACKPOT 💯 SESSION PASS 💯

🏏 {result} RUN

🅿️🅰️💲💲✔️

OWNER 👉 SHUBHAM PANDIT 💠
""".strip()


def shubham_session_loss():

    return """
❌ SESSION LOSS

DON'T WORRY ❤️

NEXT SESSION COVER 💯

OWNER 👉 SHUBHAM PANDIT 💠
""".strip()

# =========================================
# VIKAS
# =========================================

def vikas_session(over, run, call):
    emoji = session_call_emoji(call)

    return f"""CALL ME VIKAS MUMBAI 💠

{run} RUN 👉 {over} OVER

{call} KARO {emoji}

PLAY SAME LIMIT 💰
""".strip()


def vikas_session_pass(result):

    return f"""BACK TO BACK PASS 💯

🏏 {result} RUN

🅿️🅰️💲💲✔️

OWNER 👉 VIKAS MUMBAI 💠
""".strip()


def vikas_session_loss():

    return """
❌ SESSION LOSS

DON'T WORRY ❤️

NEXT SESSION COVER 💯

OWNER 👉 VIKAS MUMBAI 💠
""".strip()

# =========================================
# FIXER
# =========================================

def fixer_session(over, run, call):
    emoji = session_call_emoji(call)

    return f""" ADVANSE PASS SESSION 💯

{run} RUN 👉 {over} OVER

{call} KARO {emoji}

PLAY SAME LIMIT 💰
""".strip()


def fixer_session_pass(result):

    return f"""💯 SESSION PASS 💯

🏏 {result} RUN

🅿️🅰️💲💲✔️

OWNER 👉 FIXER BHAI 💠
""".strip()


def fixer_session_loss():

    return """
❌ SESSION LOSS

DON'T WORRY ❤️

NEXT SESSION COVER 💯

OWNER 👉 FIXER PANDIT 💠
""".strip()

# =========================================
# LOADED
# =========================================

print("✅ SESSION TEMPLATES LOADED")