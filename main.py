from dotenv import load_dotenv
load_dotenv()

from telethon import TelegramClient, events
import os
from keep_alive import keep_alive

# Replace these with your own values
api_id = os.environ['API_ID']
api_hash = os.environ['API_HASH']
phone_number = os.environ['PHONE_NUMBER']

# Create the client and connect
client = TelegramClient('session', api_id, api_hash)

# Define the auto-reply message
auto_reply_message = "Thanks for your message! I'm currently unavailable, but I'll get back to you as soon as possible."

@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):
    if event.is_private:  # only auto-reply to private chats
        from_ = await event.client.get_entity(event.from_id)
        if not from_.bot:  # don't reply to bots
            await event.reply(auto_reply_message)

async def main():
    print('Auto-reply bot is running!')
    await client.run_until_disconnected()

keep_alive()  # Add this line before the 'with client:' block

with client:
    client.loop.run_until_complete(main())
