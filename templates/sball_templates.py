# =========================================
# templates/SESSION_templates.py
# =========================================


def SESSION_call_emoji(call):
    if call == "YES":
        return "✅"
    return "❌"


# =========================================
# ROYAL
# =========================================

def royal_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""
{ball} BALL 🌐 {call} KARO {emoji}

{run} RUN 🏏

Play only on 👇

Plat at -- Www.Khelking.buzz

""".strip()


def royal_sball_pass(ball, result):

    return f"""
{result} 🅿️🅰️💲💲✔️

{ball} BALL 👑

SESSIONS PASS 💸❤️
""".strip()


def royal_sball_loss():

    return """
LOSS RAHA APNA DONT WORRY ❤️

WAIT FOR NEXT ❌
""".strip()


# =========================================
# BETTING
# =========================================

def betting_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""
{run} RUN 👍 {ball} BALL 🏏

{call} KARO {emoji}

10K LIMIT SE PLAY 🥳
""".strip()


def betting_sball_pass(ball, result):

    return f"""💫 🅱𝗢𝗢Ⓜ️ 💫 🅱𝗢𝗢Ⓜ

{result} 🅿️🅰️💲💲✔️✔️

SESSION PASS 💰🔥
""".strip()


def betting_sball_loss():

    return """
SESSION LOSS ❌
""".strip()


# =========================================
# BATMAN
# =========================================

def batman_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""BINDASS 👍
    
{ball} BALL 👉 {run} RUN

{call} KARO 👉 {emoji}

SAME LIMIT SE PLAY 💰
""".strip()


def batman_sball_pass(ball, result):

    return f"""JACKPOT 💰💰

{result} 🅿️🅰️💲💲 🤑🤑

🤑 BACK TO BACK SESSION PASS 💰
""".strip()


def batman_sball_loss():

    return """
SESSION LOSS 😒
""".strip()


# =========================================
# GAME
# =========================================

def game_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""
 🚨 ALL ACTIVE MEMBERS 🚨

 {call} KARO {emoji}

{ball} BALL 🏏 {run} RUN 

INIDAN TRUSTED SITE 👇

Www.Khelking.buzz 💯

""".strip()


def game_sball_pass(ball, result):

    return f"""
 💸 BALL SESSION PASS 💸

{result} 🅿️🅰️💲💲

🔥 TARGET HIT 🔥
""".strip()


def game_sball_loss():

    return """
LOSS ❌ KOI BAAT NHI 

NEXT SESSION 💯 CBALL HOGA 👍
""".strip()


# =========================================
# GUDDU
# =========================================

def guddu_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""

PLAY BINDASS SESSION 💰 

{run} RUN 🎯 {ball} BALL 🏏

{call} KARO {emoji}

10K LIMIT SE PLAY 💰
""".strip()


def guddu_sball_pass(ball, result):

    return f"""MUBARK HO 💯💯

{result} 🅿️🅰️💲💲✔️✔️

🏆 SESSION BALL PASSED

📊 RESULT ➜ {result}

💰 PROFIT BOOKED
""".strip()


def guddu_sball_loss():

    return """
 MISSED 😒

KEEP PATIENCE
NEXT ONE WILL CBALL IT 💯
""".strip()


# =========================================
# ROCKY
# =========================================

def rocky_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    
    return f"""
{run} RUN 👉 {ball} BALL

{call} KRO {emoji}

""".strip()


def rocky_sball_pass(ball, result):

    return f"""
🅿️🅰️💲💲🏆🏆

🏏 RESULT 👉 {result}

🏆 BACK TO BACK PASS 🏆
""".strip()

def rocky_sball_loss():

    return """
SESSION LOSS ❌

NEXT SESSION PASS ROCKY PROMISE
""".strip()


# =========================================
# PRIYANSHU
# =========================================

def priyanshu_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""
🌐 LIVE UPDATE 🌐

{run} RUN 👉 {ball} BALL 🏏

{call} KRO SAB {emoji}
""".strip()


def priyanshu_sball_pass(ball, result):

    return f"""
 {result} 🅿️🅰️💲💲🏆

💰 WINNING SESSION 💰

 WAIT FOR NEXT SESSION 💯
""".strip()

def priyanshu_sball_loss():

    return """
❌ SESSION LOSS 😊 DON'T WORRY

NEXT SESSION WILL PASS 🎯 

WAIT FOR NEXT SESSION 💯
""".strip()


# =========================================
# JACKY
# =========================================

def jacky_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""
PLAY WHIT SAME LIMIT ✔️

🏏 {run} RUN 🔻 {ball} BALL

 {call} KRO {emoji}

NAAM CHALTA HAI MARKET MEIN 🔥

""".strip()


def jacky_sball_pass(ball, result):

    return f"""
{result} RUN SESSION 🅿🅰🆂🆂 

🔻SESSIONS PASS 🔻

💣 BOOM 💣 BOOM 💣
""".strip()


def jacky_sball_loss():

    return """
SESSION WILL BE LOSS❌
""".strip()


# =========================================
# KING
# =========================================

def king_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""
🔻 SESSION LIVE 🔻

{run} RUN 👉 {ball} BALL

{call} KARO SAB {emoji}

""".strip()


def king_sball_pass(ball, result):

    return f"""
{result} RUN 🅿️🅰️💲💲

🤑 SESSIONS PASS 🤑

💣 BOOM 💣 🔻 💣 BOOM 💣

👑 KING ENTRY 👑
""".strip()


def king_sball_loss():

    return """

😒 SESSION LOSS 😒 KEEP TRUST

🎯 NEXT SESSION WILL PASS 🎯

""".strip()


# =========================================
# ANGAD
# =========================================

def angad_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""
DADA ENTRY 💠

{call} KRO SBHI {emoji}

🏏 {run} RUN in {ball} BALL
""".strip()


def angad_sball_pass(ball, result):

    return f"""
🏏 {result} RUN

💯 🅿🅰🆂🆂 💯

🏏 {result} RUN

DADA ENTRY 💠
""".strip()


def angad_sball_loss():

    return """
❌ 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 𝗟𝗢𝗦𝗦

🎯 NEXT CALL WILL BE BETTER
""".strip()


# =========================================
# RAHUL
# =========================================

def rahul_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""
✔️ SESSION CALL ✔️

{run} RUN 👉 {call} KARO SAB {emoji}

{ball} BALL 🏏 BINDASS PLAY 💰

""".strip()


def rahul_sball_pass(ball, result):

    return f"""
💯 SESSIONS PASS 💯

{result} RUN 🅿️🅰️💲💲

ACCURATE ENTRY 💯

RAHUL DADA 💠
""".strip()


def rahul_sball_loss():

    return """
🔻 SESSION LOSS 🔻

 DON'T LOSE TRUST 👍
""".strip()


# =========================================
# SHIVA
# =========================================

def shiva_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""
🔥 SHIVA REDDY  🔥

{ball} BALL 👉 {run} RUN

{call} KARO SAB {emoji}

FULL SUPPORT ❤️
""".strip()


def shiva_sball_pass(ball, result):

    return f"""
{result} RUN 🔥 SHIVA REDDY

💯 🅿🅰🆂🆂 💯

🏏 {result} RUN

👑 PERFECT CALL
""".strip()


def shiva_sball_loss():

    return """

❌ 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 𝗟𝗢𝗦𝗦

🎯 NEXT CALL WILL BE BETTER
""".strip()

# =========================================
# REDDY
# =========================================

def reddy_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""
ACTIVE ALL MEMBERS 🔔

🔻 {run} RUN | {ball} BALL

🔻 {call} KRO FATA FAT {emoji}

🔻 PALY WITH SAME LIMIT 💰
""".strip()


def reddy_sball_pass(ball, result):

    return f"""
{result} RUN SESSION 🅿️🅰️💲💲

 🔻 SESSIONS PASS 🔻
💯 BACK TO BACK PASS 💯

ONLY 👉 REDDY ANNA 💠
""".strip()


def reddy_sball_loss():

    return """
SESSION LOSS 😒

🎯 NEXT CALL SOON
""".strip()


# =========================================
# TOSSKING
# =========================================

def tossking_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""
🌐 SESSION 🌐

🏏 {run} RUN 🔻 {ball} BALL

{call} KRO SBHI {emoji}
""".strip()


def tossking_sball_pass(ball, result):

    return f"""
💯🅿🅰🆂🆂💯

🏏 {result} RUN

🔥 KING'S PERFECT CALL
""".strip()


def tossking_sball_loss():

    return """
⚠️ 🅻🅾🆂🆂 ⚠️

💎 TRUST THE PROCESS
""".strip()

# =========================================
# VIKRAM
# =========================================

def vikram_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""
🏏 VIKRAM SINGH 💠

{run} RUN 👉 {ball} BALL

{call} KARO {emoji}

PLAY SAME LIMIT 💰
""".strip()


def vikram_sball_pass(ball, result):

    return f"""
💯 SESSION PASS 💯

🏏 {result} RUN

🅿️🅰️💲💲✔️

OWNER 👉 VIKRAM SINGH 💠
""".strip()


def vikram_sball_loss():

    return """
❌ SESSION LOSS

DON'T WORRY ❤️

NEXT SESSION CBALL 💯

OWNER 👉 VIKRAM SINGH 💠
""".strip()

# =========================================
# PAWAN
# =========================================

def pawan_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""
🏏 PAWAN SINGH 💠

{run} RUN 👉 {ball} BALL

{call} KARO {emoji}

PLAY SAME LIMIT 💰
""".strip()


def pawan_sball_pass(ball, result):

    return f"""
💯 SESSION PASS 💯

🏏 {result} RUN

🅿️🅰️💲💲✔️

OWNER 👉 PAWAN SINGH 💠
""".strip()


def pawan_sball_loss():

    return """
❌ SESSION LOSS

DON'T WORRY ❤️

NEXT SESSION CBALL 💯

OWNER 👉 PAWAN SINGH 💠
""".strip()

# =========================================
# DUBAI
# =========================================

def dubai_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""

{run} RUN 👉 {ball} BALL

{call} KARO {emoji}

PLAY SAME LIMIT 💰
""".strip()


def dubai_sball_pass(ball, result):

    return f"""
💯 SESSION PASS 💯

🏏 {result} RUN

🅿️🅰️💲💲✔️

""".strip()


def dubai_sball_loss():

    return """
❌ SESSION LOSS

DON'T WORRY ❤️

NEXT SESSION CBALL 💯

""".strip()

# =========================================
# SHUBHAM
# =========================================

def shubham_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""
🏏 SHUBHAM PANDIT 💠

{run} RUN 👉 {ball} BALL

{call} KARO {emoji}

PLAY SAME LIMIT 💰
""".strip()


def shubham_sball_pass(ball, result):

    return f"""
💯 SESSION PASS 💯

🏏 {result} RUN

🅿️🅰️💲💲✔️

OWNER 👉 SHUBHAM PANDIT 💠
""".strip()


def shubham_sball_loss():

    return """
❌ SESSION LOSS

DON'T WORRY ❤️

NEXT SESSION CBALL 💯

OWNER 👉 SHUBHAM PANDIT 💠
""".strip()

# =========================================
# VIKAS
# =========================================

def vikas_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""
🏏 VIKAS MUMBAI 💠

{run} RUN 👉 {ball} BALL

{call} KARO {emoji}

PLAY SAME LIMIT 💰
""".strip()


def vikas_sball_pass(ball, result):

    return f"""
💯 SESSION PASS 💯

🏏 {result} RUN

🅿️🅰️💲💲✔️

OWNER 👉 VIKAS MUMBAI 💠
""".strip()


def vikas_sball_loss():

    return """
❌ SESSION LOSS

DON'T WORRY ❤️

NEXT SESSION CBALL 💯

OWNER 👉 VIKAS MUMBAI 💠
""".strip()

# =========================================
# FIXER
# =========================================

def fixer_sball(ball, run, call):
    emoji = SESSION_call_emoji(call)

    return f"""
🏏 FIXER PANDIT 💠

{run} RUN 👉 {ball} BALL

{call} KARO {emoji}

PLAY SAME LIMIT 💰
""".strip()


def fixer_sball_pass(ball, result):

    return f"""
💯 SESSION PASS 💯

🏏 {result} RUN

🅿️🅰️💲💲✔️

OWNER 👉 FIXER BHAI 💠
""".strip()


def fixer_sball_loss():

    return """
❌ SESSION LOSS

DON'T WORRY ❤️

NEXT SESSION CBALL 💯

OWNER 👉 FIXER BHAI 💠
""".strip()

# =========================================
# LOADED
# =========================================

print("✅ SESSION TEMPLATES LOADED")