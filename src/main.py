import os
from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')

print(f"API_ID: {api_id is not None}") # checks if api_id exsists
print(f"API_HASH: {api_hash is not None}") # checks if api_hash exsists
print(f"BOT_TOKEN: {bot_token is not None}") # checks if bot_token exsists

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

with bot:
    bot.loop.run_until_complete(bot.send_message('me', 'Hello, I\'m the FindealBot'))