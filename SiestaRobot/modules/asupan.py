# ⚠️ © @greyyvbss 

# ⚠️ Don't Remove Credits

import os

import random

from telethon.tl.types import InputMessagesFilterPhotos

from telethon.tl.types import InputMessagesFilterVideo

from telethon.tl.types import InputMessagesFilterVoice

from SiestaRobot.events import register

from SiestaRobot import telethn as tbot, ubot2 

from SiestaRobot.modules.language import gs                

@register(pattern="^/asupan ?(.*)")

async def _(event):

    memeks = await event.reply("**Sabar Kontol, Lagi Ku Cari...🔍**") 

    try:

        asupannya = [

            asupan

            async for asupan in ubot2.iter_messages(

            "@Asupan_Rzydx", filter=InputMessagesFilterVideo

            )

        ]

        kontols = random.choice(asupannya)

        pantek = await ubot2.download_media(kontols)

        await tbot.send_file(

            event.chat.id, 

            caption="Selamat Menikmati Asupanya Dek 🥵", 

            file=pantek

            )

        await memeks.delete()

    except Exception:

        await memeks.edit("Asupannya gaada koncol")


@register(pattern="^/ayang ?(.*)")

async def _(event):

    memeks = await event.reply("**Sabar Mek, Lagi Cari Ayang...🔍**") 

    try:

        asupannya = [

            asupan

            async for asupan in ubot2.iter_messages(

            "@CeweLogoPack", filter=InputMessagesFilterPhotos

            )

        ]

        kontols = random.choice(asupannya)

        pantek = await ubot2.download_media(kontols)

        await tbot.send_file(

            event.chat.id, 

            caption="Nih Ayangnya, Jan Ditakalin Ya Mek 😏", 

            file=pantek

            )

        await memeks.delete()

    except Exception:

        await memeks.edit("Haha Kasian Bet Lu Gak Punya Ayang..")


@register(pattern="^/ngaji ?(.*)")

async def _(event):

    memeks = await event.reply("**Alhamdulillah, Wait Ku Cari Dulu...🔍**") 

    try:

        asupannya = [

            asupan

            async for asupan in ubot2.iter_messages(

            "@DatabaseQuran", filter=InputMessagesFilterVoice

            )

        ]

        kontols = random.choice(asupannya)

        pantek = await ubot2.download_media(kontols)

        await tbot.send_file(

            event.chat.id, 

            caption="Dengarkan Dengan Khusyu Kak 😌", 

            file=pantek

            )

        await memeks.delete()

    except Exception:

        await memeks.edit("Lu Haram Jadi Gak Bisa Denger Qur'an..")


@register(pattern="^/ppcp ?(.*)")

async def _(event):

    memeks = await event.reply("**Sabar Tod, Lagi Gua Cari...🔍**") 

    try:

        asupannya = [

            asupan

            async for asupan in ubot2.iter_messages(

            "@ppcpdatabase", filter=InputMessagesFilterPhotos

            )

        ]

        kontols = random.choice(asupannya)

        pantek = await ubot2.download_media(kontols)

        await tbot.send_file(

            event.chat.id, 

            caption="Nih Si Paling Couple 😏", 

            file=pantek

            )

        await memeks.delete()

    except Exception:

        await memeks.edit("Tangan Lu Bau Tai, Cuci Tangan Dulu Gih..")

def helps(chat):
    return gs(chat, "asupan_help")

__mod_name__ = "ᴀsᴜᴘᴀɴ"


