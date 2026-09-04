# =========================================
# templates/cashout_templates.py
# =========================================

# =========================================
# ROYAL
# =========================================

def royal_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

👑 ROYAL WIN 👑
"""


# =========================================
# BATMAN
# =========================================

def batman_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

🦇 BATMAN OFFICIAL 🦇
"""


# =========================================
# BETTING
# =========================================

def betting_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

👑 BETTING KING 👑
"""


# =========================================
# GAME
# =========================================

def game_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

🎯 GAME CHANGER 🎯
"""


# =========================================
# GUDDU
# =========================================

def guddu_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

💎 GUDDU PANDIT 💎
"""
# =========================================
# ROCKY
# =========================================

def rocky_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

⚡ ROCKY BHAI ⚡
"""


# =========================================
# JACKY
# =========================================

def jacky_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

👑 JACKY BHAI 👑
"""


# =========================================
# PRIYANSHU
# =========================================

def priyanshu_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

💎 PRIYANSHU 💎
"""


# =========================================
# TOSSKING
# =========================================

def tossking_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

🏏 TOSS KING 🏏
"""


# =========================================
# REDDY
# =========================================

def reddy_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

❤️ REDDY ANNA ❤️
"""


# =========================================
# SHIVA
# =========================================

def shiva_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

🔱 SHIVA 🔱
"""
# =========================================
# RAHUL
# =========================================

def rahul_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

💠 RAHUL DADA 💠
"""


# =========================================
# ANGAD
# =========================================

def angad_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

⚡ ANGAD DADA ⚡
"""


# =========================================
# KING
# =========================================

def king_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

👑 THE KING 👑
"""


# =========================================
# VIKRAM
# =========================================

def vikram_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

🔥 VIKRAM 🔥
"""


# =========================================
# PAWAN
# =========================================

def pawan_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

💥 PAWAN 💥
"""


# =========================================
# DUBAI
# =========================================

def dubai_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

🌍 DUBAI THE BRAND 🌍
"""
# =========================================
# SHUBHAM
# =========================================

def shubham_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

⭐ SHUBHAM ⭐
"""


# =========================================
# VIKAS
# =========================================

def vikas_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

💎 VIKAS 💎
"""


# =========================================
# FIXER
# =========================================

def fixer_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON

🎯 FIXER 🎯
"""


# =========================================
# DEFAULT
# =========================================

def default_cashout():
    return """💸 CASH OUT 💸

✅ BOOK YOUR PROFIT

🎯 TARGET ACHIEVED

🔥 NEXT UPDATE COMING SOON
"""


# =========================================
# MAIN TEMPLATE SELECTOR
# =========================================

def get_cashout_template(channel_name):

    channel_name = channel_name.upper()

    if channel_name == "ROYAL":
        return royal_cashout()

    elif channel_name == "BATMAN":
        return batman_cashout()

    elif channel_name == "BETTING":
        return betting_cashout()

    elif channel_name == "GAME":
        return game_cashout()

    elif channel_name == "GUDDU":
        return guddu_cashout()

    elif channel_name == "ROCKY":
        return rocky_cashout()

    elif channel_name == "JACKY":
        return jacky_cashout()

    elif channel_name == "PRIYANSHU":
        return priyanshu_cashout()

    elif channel_name == "TOSSKING":
        return tossking_cashout()

    elif channel_name == "REDDY":
        return reddy_cashout()

    elif channel_name == "SHIVA":
        return shiva_cashout()

    elif channel_name == "RAHUL":
        return rahul_cashout()

    elif channel_name == "ANGAD":
        return angad_cashout()

    elif channel_name == "KING":
        return king_cashout()

    elif channel_name == "VIKRAM":
        return vikram_cashout()

    elif channel_name == "PAWAN":
        return pawan_cashout()

    elif channel_name == "DUBAI":
        return dubai_cashout()

    elif channel_name == "SHUBHAM":
        return shubham_cashout()

    elif channel_name == "VIKAS":
        return vikas_cashout()

    elif channel_name == "FIXER":
        return fixer_cashout()

    else:
        return default_cashout()