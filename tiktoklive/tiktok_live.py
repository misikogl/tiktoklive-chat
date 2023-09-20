from ahk import AHK
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent

# Instantiate the client with the user's username
client = TikTokLiveClient(unique_id="@handy.spiel")

# Instantiate AHK
ahk = AHK(executable_path='/mnt/c/Program Files/AutoHotkey/AutoHotkey.exe')

# Define how to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)
    

# Define handling an event via a "callback"
@client.on("comment")
async def on_comment(event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")

    message = event.comment.lower()

    if message == "up":
        ahk.key_press('up')

    elif message == "down":
        ahk.key_press('down')

    elif message == "left":
        ahk.key_press('left')
        ahk.key_press('left')
        ahk.key_press('left')
        ahk.key_press('left')
        ahk.key_press('left')
        ahk.key_press('left')
        ahk.key_press('left')
        ahk.key_press('left')
        ahk.key_press('left')

    elif message == "right":
        ahk.key_press('right')

    elif message == "q":
        ahk.key_press('q')

    elif message == "w":
        ahk.key_press('w')

    elif message == "e":
        ahk.key_press('e')

    elif message == "r":
        ahk.key_press('r')

    elif message == "d":
        ahk.key_press('d')

    elif message == "f":
        ahk.key_press('f')

    else:
        print("Invalid command")

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()