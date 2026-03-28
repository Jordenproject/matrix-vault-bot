from dotenv import load_dotenv
import os
from pathlib import Path

dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path, override=True)  # <-- force .env to override any existing env vars

token = os.environ.get("VAULT_TOKEN")

from vault_client import VaultCredentials
import asyncio
from nio import AsyncClient, LoginError, JoinError, RoomMessageText

creds = VaultCredentials()
HOMESERVER = "https://socialchat.metcarob.com"
# USERNAME = "@socialsocialbotjordan:socialchat.metcarob.com"
USERNAME = creds.get_username()
PASSWORD = creds.get_password()
ROOM_ID = "!dcjIEQXbuZFkAgxs:socialchat.metcarob.com"


async def message_callback(room, event):
    # Ignore messages sent by the bot itself
    if event.sender == USERNAME:
        return

    message = event.body.strip().lower()
    print(f"Received message: {message}")

    if message == "hello":
        await client.room_send(
            room_id=room.room_id,
            message_type="m.room.message",
            content={
                "msgtype": "m.text",
                "body": "goodbye",
            },
        )
        print("Replied with goodbye")


async def main():
    global client
    client = AsyncClient(HOMESERVER, USERNAME, ssl=False)

    print("Starting bot...")

    try:
        await client.login(PASSWORD)
        print("Logged in!")
    except LoginError as e:
        print("Login failed:", e)
        return

    try:
        await client.join(ROOM_ID)
        print(f"Joined room {ROOM_ID}")
    except JoinError as e:
        print("Join failed:", e)
        return

    # Register callback for text messages
    client.add_event_callback(message_callback, RoomMessageText)

    print("Listening for messages...")
    await client.sync_forever(timeout=30000)


asyncio.run(main())
