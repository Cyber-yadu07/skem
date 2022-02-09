from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hello {}

If you don't trust this bot,
1) don't read this message
2) block bot or delete chat

This Bot Works To Help You To Make Scam tag Protection Id Via Bot
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("Start Making Scam Tag id", callback_data="generate")],
        [InlineKeyboardButton(text="Home", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("Start Scam Tag Id", callback_data="generate")
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Start Making Scam Tag Id", callback_data="generate")],
        [InlineKeyboardButton("Maintaned By", url="https://t.me/Telegram")],
        [
            InlineKeyboardButton("How to use me", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
      ],
        [InlineKeyboardButton("Other bot info", url="https://t.me/bbb")],
    ]


    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - About this bot
/help - How to use this bot
/start - Start Bot
/scamtagprotectionid
/cancel - Cancel process
/restart - Restart process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to retrieve To Make Telegram Users Safe By Not Getting Scam Tag

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @Telegram
    """
