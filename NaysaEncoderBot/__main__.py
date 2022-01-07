
import time
import asyncio
import traceback
from binascii import (
    Error
)
from pyrogram import (
    Client,
    filters
)
from pyrogram.errors import (
    UserNotParticipant,
    FloodWait,
    QueryIdInvalid
)
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)
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
)   
    
from NaysaEncoderBot.plugins.admin import sts, ban, _banned_usrs, unban
from NaysaEncoderBot.forcesub import handle_force_subscribe    
    

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
        if UPDATES_CHANNEL:
          fsub = await handle_force_subscribe(bot, update)
          if fsub == 400:
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
        if UPDATES_CHANNEL:
          fsub = await handle_force_subscribe(app, message)
          if fsub == 400:
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


    # BROADCAST Admin Command
    incoming_broadcast_command = MessageHandler(
        broadcast_,
        filters=filters.command(["broadcast"]) & filters.user(AUTH_USERS) & filters.reply
    )
    app.add_handler(incoming_broadcast_command)
    @app.on_message(filters.private & filters.command("ban") & filters.user(AUTH_USERS))
    async def ban(c: Client, m: Message):
    
        if len(m.command) == 1:
            await m.reply_text(
                f"Use this command to ban any user from the bot.\n\n"
                f"Usage:\n\n"
                f"`/ban_user user_id ban_duration ban_reason`\n\n"
                f"Eg: `/ban_user 1234567 28 You misused me.`\n"
                f"This will ban user with id `1234567` for `28` days for the reason `You misused me`.",
                quote=True
            )
            return

        try:
            user_id = int(m.command[1])
            ban_duration = int(m.command[2])
            ban_reason = ' '.join(m.command[3:])
            ban_log_text = f"Banning user {user_id} for {ban_duration} days for the reason {ban_reason}."
            try:
                await c.send_message(
                    user_id,
                    f"You are banned to use this bot for **{ban_duration}** day(s) for the reason __{ban_reason}__ \n\n"
                    f"**Message from the admin**"
                )
                ban_log_text += '\n\nUser notified successfully!'
            except:
                traceback.print_exc()
                ban_log_text += f"\n\nUser notification failed! \n\n`{traceback.format_exc()}`"

            await db.ban_user(user_id, ban_duration, ban_reason)
            print(ban_log_text)
            await m.reply_text(
                ban_log_text,
                quote=True
            )
        except:
            traceback.print_exc()
            await m.reply_text(
                f"Error occoured! Traceback given below\n\n`{traceback.format_exc()}`",
                quote=True
            )


    @app.on_message(filters.private & filters.command("unban") & filters.user(AUTH_USERS))
    async def unban(c: Client, m: Message):

        if len(m.command) == 1:
            await m.reply_text(
                f"Use this command to unban any user.\n\n"
                f"Usage:\n\n`/unban_user user_id`\n\n"
                f"Eg: `/unban_user 1234567`\n"
                f"This will unban user with id `1234567`.",
                quote=True
            )
            return

        try:
            user_id = int(m.command[1])
            unban_log_text = f"Unbanning user {user_id}"
            try:
                await c.send_message(
                    user_id,
                    f"Your ban was lifted!"
                )
                unban_log_text += '\n\nUser notified successfully!'
            except:
                traceback.print_exc()
                unban_log_text += f"\n\nUser notification failed! \n\n`{traceback.format_exc()}`"
            await db.remove_ban(user_id)
            print(unban_log_text)
            await m.reply_text(
                unban_log_text,
                quote=True
            )
        except:
            traceback.print_exc()
            await m.reply_text(
                f"Error occurred! Traceback given below\n\n`{traceback.format_exc()}`",
                quote=True
            )             

    app.run()


