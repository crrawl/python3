from discord_messages import Discord_messages
from config import *

dc_messages = Discord_messages(channel_url, payload, headers)

if __name__ == "__main__":
    dc_messages.send_message()
