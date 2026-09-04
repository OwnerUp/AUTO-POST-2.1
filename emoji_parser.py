# =========================================
# EMOJI PARSER
# =========================================

import re


# =========================================
# PARSE TOSS TEAM BLOCK
# Example:
# /toss (👑 INDIA WOMEN 🔥)
# =========================================

def parse_toss_team(raw_text):

    raw_input = raw_text.replace(
        "/toss",
        "",
        1
    ).strip()

    match = re.fullmatch(
        r'\s*\((.*?)\)\s*',
        raw_input,
        flags=re.DOTALL
    )

    if not match:
        return None

    team = match.group(1).strip()

    if not team:
        return None

    return team


# =========================================
# PARSE MATCH TEAM BLOCKS
# Example:
# /match (👑 INDIA WOMEN 🔥) VS (⚡ ENGLAND WOMEN 💎) W (👑 INDIA WOMEN 🔥)
# =========================================

def parse_match(raw_text):

    raw_input = raw_text.replace(
        "/match",
        "",
        1
    ).strip()

    match = re.fullmatch(
        r'\s*\((.*?)\)\s*vs\s*\((.*?)\)\s*w\s*\((.*?)\)\s*',
        raw_input,
        flags=re.IGNORECASE | re.DOTALL
    )

    if not match:
        return None

    team1 = match.group(1).strip()
    team2 = match.group(2).strip()
    winner = match.group(3).strip()

    if not team1 or not team2 or not winner:
        return None

    return team1, team2, winner


print("✅ EMOJI PARSER LOADED")