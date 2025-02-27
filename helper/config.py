#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *
from pyrogram import Client, filters




try:
    APP_ID = 13216322
    API_HASH = "15e5e632a8a0e52251ac8c3ccbe462c7"
    BOT_TOKEN = "7160872230:AAHmmk7eDW2FwtVkRLwl3dwzJALR-qiS15Q"
    OWNER = 5642570692
    LOG = -1002175816545
    #LOG = -1001817380537
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)


from pyrogram import Client, filters

# Create the Pyrogram client (bot)
app = Client("my_bot", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Function to generate and send an invite link for the specified channel
@app.on_message(filters.command("link") & filters.private)
async def force_subscription(client, message):
    # Specify the channel ID (can be a username like "@channelname" or channel ID)
    channel_id = LOG  # e.g., @example_channel or channel ID

    try:
        # Export the invite link for the channel
        invite_link = await client.export_chat_invite_link(channel_id)
        
        print(invite_link)
    except Exception as e:
        print(e)


# Run the bot
app.run()


#try:
    # APP_ID = config("APP_ID", cast=int)
    # API_HASH = config("API_HASH")
    # BOT_TOKEN = config("BOT_TOKEN")
    # OWNER = config("OWNER_ID", default=1322549723, cast=int)
    # LOG = config("LOG_CHANNEL", cast=int)
#except Exception as e:
    # LOGS.info("Environment vars Missing")
    # LOGS.info("something went wrong")
    # LOGS.info(str(e))
    #exit(1)
    
