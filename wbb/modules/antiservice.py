# Written By [MaskedVirus | swatv3nub] for William and Ryūga
# Kang With Proper Credits

from pyrogram import filters

from wbb import app
from wbb.core.decorators.permissions import adminsOnly
from wbb.utils.dbfunctions import (
    antiservice_off,
    antiservice_on,
    is_antiservice_on,
)

__MODULE__ = "ᴀɴᴛɪ sᴇʀᴠɪᴄᴇ"
__HELP__ = """
➠ ᴘʟᴜɢɪɴ ᴛᴏ ᴅᴇʟᴇᴛᴇ sᴇʀᴠɪᴄᴇ ᴍᴇssᴀɢᴇs ɪɴ ᴀ ᴄʜᴀᴛ!

➠ /antiservice [ᴇɴᴀʙʟᴇ|ᴅɪsᴀʙʟᴇ]

➠ ᴅᴇᴠᴇʟᴏᴘ ᴀɴᴅ ᴅᴇsɪɢɴᴇᴅ ʙʏ [ᴛᴇʟᴜɢᴜ ᴄᴏᴅᴇʀs](https://t.me/telugucoders)
"""


@app.on_message(
    filters.command("antiservice")
    & ~filters.private
    & ~filters.edited
)
@adminsOnly("can_change_info")
async def anti_service(_, message):
    if len(message.command) != 2:
        return await message.reply_text(
            "ᴜsᴀɢᴇ: /antiservice [ᴇɴᴀʙʟᴇ | ᴅɪsᴀʙʟᴇ]"
        )
    status = message.text.split(None, 1)[1].strip()
    status = status.lower()
    chat_id = message.chat.id
    if status == "enable":
        await antiservice_on(chat_id)
        await message.reply_text(
            "ᴇɴᴀʙʟᴇᴅ ᴀɴᴛɪsᴇʀᴠɪᴄᴇ sʏsᴛᴇᴍ. ɪ ᴡɪʟʟ ᴅᴇʟᴇᴛᴇ sᴇʀᴠɪᴄᴇ ᴍᴇssᴀɢᴇs ғʀᴏᴍ ɴᴏᴡ ᴏɴ."
        )
    elif status == "disable":
        await antiservice_off(chat_id)
        await message.reply_text(
            "ᴅɪsᴀʙʟᴇᴅ ᴀɴᴛɪsᴇʀᴠɪᴄᴇ sʏsᴛᴇᴍ. ɪ ᴡᴏɴ'ᴛ ʙᴇ ᴅᴇʟᴇᴛɪɴɢ sᴇʀᴠɪᴄᴇ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ɴᴏᴡ ᴏɴ."
        )
    else:
        await message.reply_text(
            "ᴜɴᴋɴᴏᴡɴ sᴜғғɪx, ᴜsᴇ /antiservice [ᴇɴᴀʙʟᴇ|ᴅɪsᴀʙʟᴇ]"
        )


@app.on_message(filters.service, group=11)
async def delete_service(_, message):
    chat_id = message.chat.id
    try:
        if await is_antiservice_on(chat_id):
            return await message.delete()
    except Exception:
        pass
