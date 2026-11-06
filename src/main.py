import os
from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

print(api_id is not None) # checks if api_id exsists
print(api_id is not None) # checks if api_hash exsists