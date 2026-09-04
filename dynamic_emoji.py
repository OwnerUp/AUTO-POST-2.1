# =========================================
# DYNAMIC PREMIUM EMOJI
# =========================================

from telethon.tl.types import MessageEntityCustomEmoji


# =========================================
# UTF-16 HELPERS
# Telegram entities use UTF-16 offsets
# =========================================

def utf16_length(text):

    return len(
        text.encode("utf-16-le")
    ) // 2


def utf16_index(text, position):

    return utf16_length(
        text[:position]
    )


# =========================================
# GET CUSTOM EMOJI ENTITIES FROM COMMAND
# =========================================

def get_custom_emoji_entities(message):

    custom_emojis = []

    if not getattr(message, "entities", None):
        return custom_emojis

    for entity in message.entities:

        if isinstance(entity, MessageEntityCustomEmoji):

            custom_emojis.append({

                "offset": entity.offset,

                "length": entity.length,

                "document_id": entity.document_id

            })

    return custom_emojis


# =========================================
# CHECK CUSTOM EMOJI EXISTS
# =========================================

def has_custom_emojis(message):

    return len(
        get_custom_emoji_entities(message)
    ) > 0


# =========================================
# GET DYNAMIC EMOJIS INSIDE TOSS TEAM
#
# Example:
# /toss (👑 INDIA WOMEN 🔥)
#
# Converts command-level UTF-16 offsets
# into offsets relative to team text.
# =========================================

def get_toss_team_custom_emojis(
    message,
    team
):

    custom_emojis = get_custom_emoji_entities(
        message
    )

    if not custom_emojis:
        return []

    raw_text = getattr(
        message,
        "raw_text",
        ""
    ) or ""

    # Find exact team text inside command
    team_position = raw_text.find(team)

    if team_position == -1:
        return []

    # Team start in Telegram UTF-16 units
    team_start_utf16 = utf16_index(
        raw_text,
        team_position
    )

    team_length_utf16 = utf16_length(
        team
    )

    result = []

    for entity in custom_emojis:

        relative_offset = (
            entity["offset"]
            - team_start_utf16
        )

        # Keep only emojis located inside team block
        if (
            relative_offset >= 0
            and
            relative_offset < team_length_utf16
        ):

            result.append({

                "offset": relative_offset,

                "length": entity["length"],

                "document_id": entity["document_id"]

            })

    return result


# =========================================
# BUILD DYNAMIC ENTITIES FOR FINAL TEXT
#
# Finds every occurrence of team in caption/promo
# and places captured Premium Emojis there.
# =========================================

def build_dynamic_team_entities(
    text,
    team,
    team_custom_emojis
):

    entities = []

    if not text:
        return entities

    if not team:
        return entities

    if not team_custom_emojis:
        return entities

    current = 0

    while True:

        team_position = text.find(
            team,
            current
        )

        if team_position == -1:
            break

        team_start_utf16 = utf16_index(
            text,
            team_position
        )

        for emoji in team_custom_emojis:

            entities.append(

                MessageEntityCustomEmoji(

                    offset=(
                        team_start_utf16
                        + emoji["offset"]
                    ),

                    length=emoji["length"],

                    document_id=emoji[
                        "document_id"
                    ]

                )

            )

        current = (
            team_position
            + len(team)
        )

    return entities
# =========================================
# GET CUSTOM EMOJIS FOR ANY TEXT BLOCK
# MATCH: TEAM1 / TEAM2 / WINNER
# =========================================

def get_text_custom_emojis(
    message,
    target_text,
    occurrence=1
):

    custom_emojis = get_custom_emoji_entities(
        message
    )

    if not custom_emojis:
        return []

    raw_text = getattr(
        message,
        "raw_text",
        ""
    ) or ""

    # =====================================
    # FIND REQUIRED OCCURRENCE
    # =====================================

    search_from = 0
    target_position = -1

    for _ in range(occurrence):

        target_position = raw_text.find(
            target_text,
            search_from
        )

        if target_position == -1:
            return []

        search_from = (
            target_position
            + len(target_text)
        )

    # =====================================
    # CONVERT TARGET START TO UTF-16
    # =====================================

    target_start_utf16 = utf16_index(
        raw_text,
        target_position
    )

    target_length_utf16 = utf16_length(
        target_text
    )

    result = []

    # =====================================
    # KEEP EMOJIS INSIDE TARGET
    # =====================================

    for entity in custom_emojis:

        relative_offset = (
            entity["offset"]
            - target_start_utf16
        )

        if (
            relative_offset >= 0
            and
            relative_offset < target_length_utf16
        ):

            result.append({

                "offset": relative_offset,

                "length": entity["length"],

                "document_id": entity["document_id"]

            })

    return result




print("✅ DYNAMIC EMOJI LOADED")