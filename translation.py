from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):



    START_TEXT = """
Hey {} 

I am Telegram Most Powerful Media Encoder Bot

I can Encode Any Video or File in Negligible Quality

Use Help Command to Know How to Use me

Made With 💕 By @Tellybots_4u
"""
    HELP_TEXT = """
Recommended
➠ Just Send Me Media To Get Started

Set Thumbnail
➠ Send Thumbnail To Set Thumbnail

Made With 💕 By @Tellybots_4u
"""
    ABOUT_TEXT = """
🤖 My Name : Media-Encoder-Bot\n
🚦 Version : <a href='https://telegram.me/tellybots_4u'>2.5</a>\n
💫 Source Code : <a href='https://t.me/tellybots_digital'>Click Here</a>\n
🗃️ Library : <a href='https://pyrogram.org'>Click Here</a>\n
👲 Developer : <a href='https://telegram.me/tellybots_4u'>TellyBots_4u</a>\n
📦 Last Updated : <a href='https://telegram.me/tellybots_4u'>[ 07-Jan-22 ] 08:00 AM</a>"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 Update Channel', url='https://telegram.me/tellybots_4u'),
        InlineKeyboardButton('💬 Support Group', url='https://telegram.me/tellybots_support')
        ],[
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
