"""
MIT License

Copyright (c) 2021 TheHamkerCat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import os

from pyrogram import filters

from wbb import app
from wbb.core.decorators.permissions import adminsOnly

__MODULE__ = "ᴀᴅᴍɪɴ ᴍɪsᴄ"
__HELP__ = """
➠ /set_chat_title - ᴄʜᴀɴɢᴇ ᴛʜᴇ ɴᴀᴍᴇ ᴏғ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ.
➠ /set_chat_photo - ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴘғᴘ ᴏғ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ.
➠ /set_user_title - ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀ ᴛɪᴛʟᴇ ᴏғ ᴀɴ ᴀᴅᴍɪɴ.
"""


@app.on_message(
    filters.command("set_chat_title")
    & ~filters.private
    & ~filters.edited
)
@adminsOnly("can_change_info")
async def set_chat_title(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**ᴜsᴀɢᴇ:**\n/set_chat_title ɴᴇᴡ ɴᴀᴍᴇ")
    old_title = message.chat.title
    new_title = message.text.split(None, 1)[1]
    await message.chat.set_title(new_title)
    await message.reply_text(
        f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ɢʀᴏᴜᴘ ᴛɪᴛʟᴇ ғʀᴏᴍ {old_title} ᴛᴏ {new_title}"
    )


@app.on_message(
    filters.command("set_user_title")
    & ~filters.private
    & ~filters.edited
)
@adminsOnly("can_change_info")
async def set_user_title(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴛᴏ sᴇᴛ ʜɪs ᴀᴅᴍɪɴ ᴛɪᴛʟᴇ"
        )
    if not message.reply_to_message.from_user:
        return await message.reply_text(
            "ɪ ᴄᴀɴ'ᴛ ᴄʜᴀɴɢᴇ ᴀᴅᴍɪɴ ᴛɪᴛʟᴇ ᴏғ ᴀɴ ᴜɴᴋɴᴏᴡɴ ᴇɴᴛɪᴛʏ"
        )
    chat_id = message.chat.id
    from_user = message.reply_to_message.from_user
    if len(message.command) < 2:
        return await message.reply_text(
            "**ᴜsᴀɢᴇ:**\n/set_user_title ɴᴇᴡ ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀ ᴛɪᴛʟᴇ"
        )
    title = message.text.split(None, 1)[1]
    await app.set_administrator_title(chat_id, from_user.id, title)
    await message.reply_text(
        f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ {from_user.mention}'s ᴀᴅᴍɪɴ ᴛɪᴛʟᴇ ᴛᴏ {title}"
    )


@app.on_message(
    filters.command("set_chat_photo")
    & ~filters.private
    & ~filters.edited
)
@adminsOnly("can_change_info")
async def set_chat_photo(_, message):
    reply = message.reply_to_message

    if not reply:
        return await message.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ sᴇᴛ ɪᴛ ᴀs ᴄʜᴀᴛ_ᴘʜᴏᴛᴏ"
        )

    file = reply.document or reply.photo
    if not file:
        return await message.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴅᴏᴄᴜᴍᴇɴᴛ ᴛᴏ sᴇᴛ ɪᴛ ᴀs chat_photo"
        )

    if file.file_size > 5000000:
        return await message.reply("ғɪʟᴇ sɪᴢᴇ ᴛᴏᴏ ʟᴀʀɢᴇ.")

    photo = await reply.download()
    await message.chat.set_photo(photo)
    await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ɢʀᴏᴜᴘ ᴘʜᴏᴛᴏs")
    os.remove(photo)
