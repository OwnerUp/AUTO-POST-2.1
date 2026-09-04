# ============================================================
# AUTO POST 7 - HYBRID STARTUP
# User session = posting engine
# Bot session  = Telegram button/control panel
# ============================================================
import os
import sys
import asyncio
from telethon import TelegramClient

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from config import API_ID, API_HASH, PHONE, SESSION_NAME, BOT_TOKEN, BOT_SESSION_NAME

from handlers.league_handler import register_league_handler
from handlers.toss_handler import register_toss_handler
from handlers.toss_pass import register_toss_pass_handler
from handlers.delete_toss import register_delete_toss_handler
from handlers.match_handler import register_match_handler
from handlers.match_pass import register_match_pass_handler
from handlers.delete_match import register_delete_match_handler
from handlers.edit_toss import register_edit_toss_handler
from handlers.edit_match import register_edit_match_handler
from handlers.session_handler import register_session_handler
from handlers.sball_handler import register_sball_handler
from handlers.session_pass import register_session_pass_handler
from handlers.sbpass_handler import register_sbpass_handler
from handlers.session_loss import register_session_loss_handler
from handlers.sbloss_handler import register_sball_loss_handler
from handlers.entry_handler import register_entry_handler
from handlers.inning_break_handler import register_inning_break_handler
from handlers.cashout_handler import register_cashout_handler
from addchannel_handler import register_addchannel_handler

USER_SESSION_PATH = os.path.join(ROOT_DIR, SESSION_NAME)
BOT_SESSION_PATH = os.path.join(ROOT_DIR, BOT_SESSION_NAME)

user_client = TelegramClient(USER_SESSION_PATH, API_ID, API_HASH)
bot_client = TelegramClient(BOT_SESSION_PATH, API_ID, API_HASH)

# All existing posting commands stay on the user account.
register_league_handler(user_client)
register_toss_handler(user_client)
register_toss_pass_handler(user_client)
register_match_handler(user_client)
register_match_pass_handler(user_client)
register_delete_toss_handler(user_client)
register_delete_match_handler(user_client)
register_edit_toss_handler(user_client)
register_edit_match_handler(user_client)
register_session_handler(user_client)
register_sball_handler(user_client)
register_session_pass_handler(user_client)
register_sbpass_handler(user_client)
register_session_loss_handler(user_client)
register_sball_loss_handler(user_client)
register_entry_handler(user_client)
register_inning_break_handler(user_client)
register_cashout_handler(user_client)

async def main():
    if not BOT_TOKEN or BOT_TOKEN.startswith('PASTE_'):
        raise RuntimeError('BOT_TOKEN missing. Put your BotFather token in config.py or environment variable BOT_TOKEN.')

    await user_client.start(phone=PHONE)
    me = await user_client.get_me()

    # The real bot owns the inline-button UI. It is restricted to the same
    # Telegram account that owns the posting session.
    register_addchannel_handler(bot_client, owner_id=me.id)
    await bot_client.start(bot_token=BOT_TOKEN)
    bot_me = await bot_client.get_me()

    print(f'✅ USER SESSION: {me.first_name} (id={me.id})')
    print(f'✅ CONTROL BOT: @{bot_me.username or bot_me.first_name}')
    print('🚀 AUTO POST 7 STARTED')
    print('📱 Open the control bot in Telegram and send /start')

    await asyncio.gather(
        user_client.run_until_disconnected(),
        bot_client.run_until_disconnected(),
    )

if __name__ == '__main__':
    with user_client:
        user_client.loop.run_until_complete(main())
