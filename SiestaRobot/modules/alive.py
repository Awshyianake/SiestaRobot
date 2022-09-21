import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/c880f57deef159e1e9b6c.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜɪ [{event.sender.first_name}](tg://user?id={event.sender.id}), ɪ'ᴍ ɴɪsᴋᴀʟᴀ.** \n"
  TEXT += "**ɪ'ᴍ ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ** \n\n"
  TEXT += f"♡ **ᴍʏ ᴍᴀsᴛᴇʀ : [ꝛᴢʏᴅx](https://t.me/ShinzoShitsuren)** \n"
  TEXT += f"♡ **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n"
  TEXT += f"♡ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n"
  TEXT += f"♡ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  TEXT += "**ᴛʜᴀɴᴋs ꜰᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ʜᴇʀᴇ 😉**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/NiskalaXRobot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/NiskalaSupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
