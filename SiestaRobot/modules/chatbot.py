import requests
from pyrogram import filters
from pyrogram.types import Message
from googletrans import Translator
from SiestaRobot import BOT_ID
from SiestaRobot.utils.filter_groups import cbot
from SiestaRobot.ex_plugins import get_command
from SiestaRobot.utils.lang import language
from SiestaRobot.mongo import chatb
from SiestaRobot.utils.custom_filters import admin_filter
from button import Chat_Bot
from SiestaRobot.modules.language import gs


tr = Translator()
CBOT = get_command("CBOT")
CBOTA = get_command("CBOTA")


@app.on_message(filters.command("chatbot") & ~filters.private& admin_filter)
@language
async def cbots(client, message: Message, _):
    group_id = str(message.chat.id)
    chat_id = message.chat.id
    user_id = message.from_user.id
    user = await app.get_chat_member(group_id, user_id)
    if not user.status == "creator" or user.status == "administrator":
        return
    if len(message.command) < 2:
        return await message.reply_text(_["chatb1"])
    status = message.text.split(None, 1)[1].strip()
    status = status.lower()
    args = get_arg(message)
    sex = await message.reply_text(_["antil2"])
    lower_args = args.lower()
    if lower_args == "on":
        chatb.insert_one({f"chatbot": group_id})
    elif lower_args == "off":
        chatb.delete_one({f"chatbot": group_id})
    else:
        return await sex.edit(_["chatb1"])
    await sex.edit(f"✅ **Successfully** `{'Enabled' if lower_args=='on' else 'Disabled'}` ** Chat bot**")

@app.on_message(filters.text & filters.reply & ~filters.bot & ~filters.via_bot & ~filters.forwarded & ~filters.private , group=cbot)
async def szcbot(_, message: Message):
    chat_id = message.chat.id
    if not message.reply_to_message:
        return
    if not message.reply_to_message.from_user:
        return
    if message.reply_to_message.from_user.id != BOT_ID:
        return
    if message.text[0] == "/":
        return
    chat = chatb.find_one({"chatbot":chat_id})   
    if chat:
        await app.send_chat_action(message.chat.id, "typing")
        try:
           lang = tr.translate(message.text).src
           trtoen = (message.text if lang=="en" else tr.translate(message.text, dest="en").text).replace(" ", "%20")
           text = trtoen.replace(" ", "%20") if len(message.text) < 2 else trtoen
           affiliateplus = requests.get(f"https://api.affiliateplus.xyz/api/chatbot?message={text}&botname=Rose&ownername=@supunma&user={chat_id}")
           textmsg = (affiliateplus.json()["message"])
           if "Affiliate+" in textmsg:
               textmsg = textmsg.replace("Affiliate+", "Niskala")
           if "Lebyy_Dev" in textmsg:
               textmsg = textmsg.replace("Lebyy_Dev", "Rzydx")
           if "God Brando" in textmsg:
               textmsg = textmsg.replace("God Brando", f"{message.from_user.first_name}")
           if "seeker" in textmsg:
               textmsg = textmsg.replace("seeker", f"wow")
           msg = tr.translate(textmsg, src='en', dest=lang)
           await message.reply_text(msg.text)
        except Exception:
           user_id = message.from_user.id
           lang = tr.translate(message.text).src
           trtoen = (message.text if lang=="en" else tr.translate(message.text, dest="en").text).replace(" ", "%20")
           text = trtoen.replace(" ", "%20") if len(message.text) < 2 else trtoen
           safeone = requests.get(f"https://api.safone.tech/chatbot?query=Niskala&user_id=1854013237&bot_name=Niskala&bot_master=envparse")
           textmsg = (safeone.json()["answer"])
           if "Affiliate+" in textmsg:
               textmsg = textmsg.replace("Affiliate+", "Niskala")
           if "[Safone]" in textmsg:
               textmsg = textmsg.replace("[Safone]", "Rzydx")
           msg = tr.translate(textmsg, src='en', dest=lang)
           await message.reply_text(msg.text)

def helps(chat):
    return gs(chat, "chatbot_help")

__mod_name__ = "ᴄʜᴀᴛʙᴏᴛ"
