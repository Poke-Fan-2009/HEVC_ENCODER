from pyrogram.types import Message
import time
import time
from datetime import datetime as dt
import os
from NaysaEncoderBot import (
    APP_ID,
    API_HASH,
    AUTH_USERS,
    DOWNLOAD_LOCATION,
    LOGGER,
    TG_BOT_TOKEN,
    BOT_USERNAME,
    SESSION_NAME,
    DATABASE_URL,
    data,
    app,
    crf,
    resolution,
    audio_b,
    preset,
    codec,
    watermark,
    UPDATES_CHANNEL

from NaysaEncoderBot.plugins.admin import sts, ban, _banned_usrs, unban
    
    
    
    

from NaysaEncoderBot.plugins.broadcast import (
    broadcast_
)
from NaysaEncoderBot.database import Database
import os, time, asyncio, json
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.types import ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, \
    PeerIdInvalid
db = Database(DATABASE_URL, SESSION_NAME)
CURRENT_PROCESSES = {}
CHAT_FLOOD = {}
broadcast_ids = {}
from NaysaEncoderBot.helper_funcs.utils import add_task, on_task_complete
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from translation import Translation
from NaysaEncoderBot.plugins.incoming_message_fn import (
    incoming_start_message_f,
    incoming_compress_message_f,
    incoming_cancel_message_f
)

from NaysaEncoderBot.plugins.status_message_fn import (
    eval_message_f,
    exec_message_f,
    upload_log_file
)
import logging
logger = logging.getLogger(__name__)
from NaysaEncoderBot.commands import Command

sudo_users = "1666551439" 
crf.append("30")
codec.append("libx265")
resolution.append("1280x720")
preset.append("veryfast")
audio_b.append("30k")
# 🤣

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
uptime = dt.now()

def ts(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + "d, ") if days else "")
        + ((str(hours) + "h, ") if hours else "")
        + ((str(minutes) + "m, ") if minutes else "")
        + ((str(seconds) + "s, ") if seconds else "")
        + ((str(milliseconds) + "ms, ") if milliseconds else "")
    )
    return tmp[:-2]


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    #
    
    
    #
    app.set_parse_mode("html")
    #
    # STATUS ADMIN Command

    # START command

    
   
    @app.on_message(filters.incoming & filters.command(["start", f"start@{BOT_USERNAME}"]))
    async def start(bot, update):                          
        if not await db.is_user_exist(update.chat.id):
            await db.add_user(update.chat.id)
        if UPDATES_CHANNEL is not None:
            message = update
            client = bot
            try:
                user = await client.get_chat_member(UPDATES_CHANNEL, message.chat.id)
                if user.status == "kicked":
                    await message.reply_text(
                        text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/linux_repo).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await message.reply_text(
                    text="**Please Join My Updates Channel to use this Bot!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await message.reply_text(
                    text="Something went Wrong. Contact my [Support Group](https://t.me/linux_repo).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return        
        await update.reply_text(
            text=Translation.START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=Translation.START_BUTTONS
        )     
 
    @app.on_message(filters.incoming & filters.command(["restart", f"restart@{BOT_USERNAME}"]))
    async def restarter(app, message):
        if message.from_user.id in AUTH_USERS:
            await message.reply_text("•Restarting")
            quit(1)
        
    @app.on_message(filters.incoming & filters.command(["clear", f"clear@{BOT_USERNAME}"]))
    async def restarter(app, message):
      data.clear()
      await message.reply_text("Successfully cleared Queue ...")
         
    @app.on_message(filters.incoming & (filters.video | filters.document))
    async def help_message(app, message):        
        if not await db.is_user_exist(message.chat.id):
            await db.add_user(message.chat.id)
        if UPDATES_CHANNEL is not None:
            message = message
            client = app
            try:
                user = await client.get_chat_member(UPDATES_CHANNEL, message.chat.id)
                if user.status == "kicked":
                    await message.reply_text(
                        text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/linux_repo).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await message.reply_text(
                    text="**Please Join My Updates Channel to use this Bot!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await message.reply_text(
                    text="Something went Wrong. Contact my [Support Group](https://t.me/linux_repo).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return        
        query = await message.reply_text("Added to Queue ⏰...\nPlease be patient, Compress will start soon", quote=True)
        data.append(message)
        if len(data) == 1:
         await query.delete()   
         await add_task(message)            
    @app.on_message(filters.incoming & (filters.photo))
    async def help_message(app, message):
        os.system('rm thumb.jpg')
        await message.download(file_name='/app/thumb.jpg')
        await message.reply_text('Thumbnail Added')
        
    @app.on_callback_query()
    async def button(bot, update):
        if update.data == "home":
            await update.message.edit_text(
                text=Translation.START_TEXT.format(update.from_user.mention),
                reply_markup=Translation.START_BUTTONS,
                disable_web_page_preview=True
            )
        elif update.data == "help":
            await update.message.edit_text(
                text=Translation.HELP_TEXT,
                reply_markup=Translation.HELP_BUTTONS,
                disable_web_page_preview=True
            )
        elif update.data == "about":
            await update.message.edit_text(
                text=Translation.ABOUT_TEXT,
                reply_markup=Translation.ABOUT_BUTTONS,
                disable_web_page_preview=True
            )
        else:
            await update.message.delete()
  
    @app.on_message(filters.incoming & filters.command(["log", f"log@{BOT_USERNAME}"]))
    async def help_message(app, message):
        await upload_log_file(app, message)
    @app.on_message(filters.incoming & filters.command(["ping", f"ping@{BOT_USERNAME}"]))
    async def up(app, message):
      stt = dt.now()
      ed = dt.now()
      v = ts(int((ed - uptime).seconds) * 1000)
      ms = (ed - stt).microseconds / 1000
      p = f"🌋Pɪɴɢ = {ms}ms"
      await message.reply_text(v + "\n" + p)


     #
    # STATUS ADMIN Command
    incoming_status_command = MessageHandler(
        sts,
        filters=filters.command(["status"]) & filters.user(AUTH_USERS)
    )
    app.add_handler(incoming_status_command)

    # BAN Admin Command
    incoming_ban_command = MessageHandler(
        ban,
        filters=filters.command(["ban_user"]) & filters.user(AUTH_USERS)
    )
    app.add_handler(incoming_ban_command)

    # UNBAN Admin Command
    incoming_unban_command = MessageHandler(
        unban,
        filters=filters.command(["unban_user"]) & filters.user(AUTH_USERS)
    )
    app.add_handler(incoming_unban_command)

    # BANNED_USERS Admin Command
    incoming_banned_command = MessageHandler(
        _banned_usrs,
        filters=filters.command(["banned_users"]) & filters.user(AUTH_USERS)
    )
    app.add_handler(incoming_banned_command)

    # BROADCAST Admin Command
    incoming_broadcast_command = MessageHandler(
        broadcast_,
        filters=filters.command(["broadcast"]) & filters.user(AUTH_USERS) & filters.reply
    )
    app.add_handler(incoming_broadcast_command)
             

    app.run()


