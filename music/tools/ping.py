from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from strings import get_command
from strings.filters import command
from AnonX import app
from AnonX.core.call import Anon 
from AnonX.utils import bot_sys_stats
from AnonX.utils.decorators.language import language, languageCB

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(command(PING_COMMAND) & filters.group & ~filters.edited & ~BANNED_USERS
)
@languageCB
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await Yukki.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            MUSIC_BOT_NAME, resp, UP, DISK, CPU, RAM, pytgping
        )
    )
