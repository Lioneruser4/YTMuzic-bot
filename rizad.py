from pyrogram import Client
import os

BOT_TOKEN = ("2138035413:AAFUuaAoCSdauCOyo8eB0kgCsFHbai9IfEY")
    
    if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    bot = Client(
        "YT-Muzic",
        bot_token=BOT_TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
    )
    bot.run()
