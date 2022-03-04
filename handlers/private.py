import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/92dd93f98c61c63c6f100.jpg",
        caption=f"""**𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 🥀𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 🎶 𝐁𝐨𝐭 𝐑𝐮𝐧 𝐎𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 🥀 𝐕𝐩𝐬 💫𝐒𝐞𝐫𝐯𝐞𝐫 🌎 𝐅𝐞𝐞𝐥 ❤️ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎧 𝐈𝐧 𝐕𝐜 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 = [༄🦄ᶦᶰᵈ᭄༂❦͟𝑨𝑺𝑯𝑹𝑨𝑭⋆͟ᶜ͟ᴿ͟ᴬ͟ᶻ͟ᴵ͟ᴱ͟ᚸ⃝⃘⃟⃠̰̃ᴷ͟ᵞ͟ᴬ͟ᵀ͟༄༂✰💞▓࿐](https://t.me/itz_me_monuuz)

𝐂𝐫𝐞𝐚𝐭𝐨𝐫 :- [💞 ༄🦄ᶦᶰᵈ᭄༂❦͟𝑨𝑺𝑯𝑹𝑨𝑭⋆͟ᶜ͟ᴿ͟ᴬ͟ᶻ͟ᴵ͟ᴱ͟ᚸ⃝⃘⃟⃠̰̃ᴷ͟ᵞ͟ᴬ͟ᵀ͟༄༂✰💞▓࿐](https://t.me/itz_me_monuuz)
𝐒𝐮𝐩𝐩𝐨𝐫𝐭 :- [💞  𝗦𝗽𝗼𝗿𝘁 𝗕𝗼𝗧𝘀 ❤️🎸](https://t.me/moluuzsupport)
𝐃𝐢𝐬𝐜𝐮𝐬𝐬 :- [💞  𝗦𝗽𝗼𝗿𝘁 𝗖𝗹𝗮𝗻 🎧](https://t.me/moluuzsupport)
𝐒𝐨𝐮𝐫𝐜𝐞  :- [💞  𝗖𝗹𝗶𝗰𝗸 ☑️ 𝗥𝗲𝗽𝗼 🌍](https://github.com/itzmemonuuz123/SmokerMusicX)
𝐂𝐨𝐦𝐦𝐚𝐧𝐝 :- [💞 𝗖𝗹𝗶𝗰𝗸 ☑️ 𝗡𝗼𝘄 🚩](https://telegra.ph/%EA%9C%B1%E1%B4%8D%E1%B4%8F%E1%B4%8B%E1%B4%87%CA%80-%E1%B4%8D%E1%B4%9C%EA%9C%B1%C9%AA%E1%B4%84-%CA%99%E1%B4%8F%E1%B4%9B-%E1%B4%84%E1%B4%8F%E1%B4%8D%E1%B4%8D%E1%B4%80%C9%B4%E1%B4%85%EA%9C%B1-08-29)
GIFSchannel :- [💞 𝗝𝗼𝗶𝗻 ❤️🥀](https://t.me/cutebabygif916)

𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [༄🦄ᶦᶰᵈ᭄༂❦͟𝑨𝑺𝑯𝑹𝑨𝑭⋆͟ᶜ͟ᴿ͟ᴬ͟ᶻ͟ᴵ͟ᴱ͟ᚸ⃝⃘⃟⃠̰̃ᴷ͟ᵞ͟ᴬ͟ᵀ͟༄༂✰💞▓࿐](https://t.me/itz_me_monuuz)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 Jᴏɪɴ Hᴇʀᴇ & Sᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/esport_bots")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/92dd93f98c61c63c6f100.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Cʟɪᴄᴋ Mᴇ Tᴏ Gᴇᴛ Rᴇᴘᴏ 💞", url=f"https://github.com/itzmemonuuz123/SmokerMusicX")
                ]
            ]
        ),
    )
