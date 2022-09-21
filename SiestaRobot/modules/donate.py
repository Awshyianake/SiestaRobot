import os
import re
from platform import python_version as kontol
from telethon import events, Button
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/c880f57deef159e1e9b6c.jpg"

@register(pattern=("/donate"))
async def awake(event):
  TEXT = f"ʙᴀɢɪ ᴋᴀᴍᴜ ʏᴀɴɢ ɪɴɢɪɴ ʙᴇʀᴅᴏɴᴀsɪ ᴜɴᴛᴜᴋ ɴɪsᴋᴀʟᴀ ʀᴏʙᴏᴛ, sɪʟᴀʜᴋᴀɴ ᴋʟɪᴋ ᴅɪʙᴀᴡᴀʜ ɪɴɪ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀɴᴛᴜ ᴍᴇɴsᴜᴘᴘᴏʀᴛ ᴀɢᴀʀ ʙᴏᴛ ᴛᴇᴛᴀᴘ sᴇʜᴀᴛ ᴋᴜᴀᴛ ᴛᴀʜᴀɴ ʟᴀᴍᴀ ᴅᴀɴ ᴍᴇᴍʙᴀɴᴛᴜ ᴍᴇɴᴇᴍᴀɴɪ ᴋᴀᴍᴜ ʙᴇʀᴀᴋᴛɪꜰɪᴛᴀs ᴅɪ ᴛᴇʟᴇɢʀᴀᴍ 😉"
  BUTTON = [[Button.url("ᴅᴏɴᴀᴛᴇ 🎁", "https://t.me/ShinzoShitsuren")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
