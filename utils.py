# =========================================
# utils.py
# =========================================

from io import BytesIO

from telethon.errors.rpcerrorlist import (
    DocumentInvalidError,
    MessageNotModifiedError
)

from emoji_engine import premium_entities
from dynamic_emoji import build_dynamic_team_entities


# =========================================
# BUILD ALL ENTITIES
# STATIC + TOSS DYNAMIC + MATCH DYNAMIC
# =========================================

def build_all_entities(
    text,
    channel_name,
    dynamic_team=None,
    dynamic_emojis=None,
    dynamic_items=None,
    template_entities=None
):

    # =====================================
    # STATIC PREMIUM EMOJIS
    # =====================================

    entities = premium_entities(
        text,
        channel_name
    )

    # =====================================
    # SINGLE DYNAMIC TEAM
    # TOSS SUPPORT
    # =====================================

    if dynamic_team and dynamic_emojis:

        dynamic_entities = build_dynamic_team_entities(
            text,
            dynamic_team,
            dynamic_emojis
        )

        entities.extend(dynamic_entities)

    # =====================================
    # MULTIPLE DYNAMIC ITEMS
    # MATCH / ENTRY SUPPORT
    # =====================================

    if dynamic_items:

        for item in dynamic_items:

            item_text = item.get("text")
            item_emojis = item.get("emojis")

            if not item_text:
                continue

            if not item_emojis:
                continue

            dynamic_entities = build_dynamic_team_entities(
                text,
                item_text,
                item_emojis
            )

            entities.extend(dynamic_entities)

    # Saved template formatting/entities (from Add Channel wizard)
    if template_entities:
        entities.extend(template_entities)

    # =====================================
    # REMOVE DUPLICATE CUSTOM EMOJIS
    # =====================================

    unique_entities = []

    seen_custom = set()

    for entity in entities:

        if hasattr(entity, "document_id"):

            key = (
                entity.offset,
                entity.length,
                entity.document_id
            )

            if key in seen_custom:
                continue

            seen_custom.add(key)

        unique_entities.append(entity)

    # =====================================
    # DEBUG
    # =====================================

    print("=" * 60)
    print("CHANNEL :", channel_name)
    print("TEXT :")
    print(text)
    print()

    for entity in unique_entities:

        print(
            type(entity).__name__,
            vars(entity)
        )

    print("=" * 60)

    return unique_entities

# =========================================
# SAFE MEDIA SEND
# =========================================

async def send_media_safe(
    client,
    channel,
    reply_msg,
    caption,
    channel_name,
    dynamic_team=None,
    dynamic_emojis=None,
    dynamic_items=None,
    reply_to=None,
    template_entities=None
):

    entities = build_all_entities(
        caption,
        channel_name,
        dynamic_team,
        dynamic_emojis,
        dynamic_items,
        template_entities
    )

    # ==========================
    # DEBUG
    # ==========================

    print("\n" + "=" * 60)
    print("SENDING MEDIA :", channel_name)
    print("CAPTION :\n")
    print(caption)
    print("\nENTITIES :")

    for e in entities:
        print(type(e).__name__, vars(e))

    print("=" * 60 + "\n")

    try:

        return await client.send_file(
            channel,
            file=reply_msg.media,
            caption=caption,
            formatting_entities=entities,
            parse_mode=None,
            reply_to=reply_to
        )

    except DocumentInvalidError:

        media_stream = BytesIO()

        await reply_msg.download_media(
            file=media_stream
        )

        media_stream.seek(0)

        return await client.send_file(
            channel,
            file=media_stream,
            caption=caption,
            formatting_entities=entities,
            parse_mode=None,
            reply_to=reply_to
        )
    # =========================================
# SAFE TEXT SEND
# =========================================

async def send_text_safe(
    client,
    channel,
    text,
    reply_to,
    channel_name,
    dynamic_team=None,
    dynamic_emojis=None,
    dynamic_items=None,
    template_entities=None
):

    entities = build_all_entities(
        text,
        channel_name,
        dynamic_team,
        dynamic_emojis,
        dynamic_items,
        template_entities
    )

    print("\n" + "=" * 60)
    print("SENDING TEXT :", channel_name)
    print(text)
    print("\nENTITIES :")

    for e in entities:
        print(type(e).__name__, vars(e))

    print("=" * 60 + "\n")

    return await client.send_message(
        channel,
        text,
        reply_to=reply_to,
        formatting_entities=entities,
        parse_mode=None,
        link_preview=False
    )


# =========================================
# SAFE TEXT EDIT
# =========================================

async def edit_text_safe(
    client,
    channel,
    message_id,
    text,
    channel_name,
    dynamic_team=None,
    dynamic_emojis=None,
    dynamic_items=None
):

    entities = build_all_entities(
        text,
        channel_name,
        dynamic_team,
        dynamic_emojis,
        dynamic_items
    )

    try:

        return await client.edit_message(
            channel,
            message_id,
            text,
            formatting_entities=entities,
            parse_mode=None,
            link_preview=False
        )

    except MessageNotModifiedError:

        return

    # =========================================
# SAFE MEDIA EDIT
# =========================================

async def edit_media_safe(
    client,
    channel,
    message_id,
    caption,
    channel_name,
    dynamic_team=None,
    dynamic_emojis=None,
    dynamic_items=None
):

    entities = build_all_entities(
        caption,
        channel_name,
        dynamic_team,
        dynamic_emojis,
        dynamic_items
    )

    print("\n" + "=" * 60)
    print("EDITING MEDIA :", channel_name)
    print(caption)
    print("\nENTITIES :")

    for e in entities:
        print(type(e).__name__, vars(e))

    print("=" * 60 + "\n")

    try:

        return await client.edit_message(
            channel,
            message_id,
            text=caption,
            formatting_entities=entities,
            parse_mode=None
        )

    except MessageNotModifiedError:

        return


print("✅ UTILS LOADED")