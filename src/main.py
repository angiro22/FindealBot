import os
from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

print(f"API_ID: {api_id is not None}") # checks if api_id exsists
print(f"API_HASH: {api_hash is not None}") # checks if api_hash exsists

with TelegramClient('', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hello World'))