import os

from os import path

from pyrogram import Client, filters

from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup

from pyrogram.errors import UserAlreadyParticipant

from callsmusic import callsmusic, queues

from callsmusic.callsmusic import client as USER

from helpers.admins import get_administrators

import requests

import aiohttp

from youtube_search import YoutubeSearch

import converter

from downloaders import youtube

from config import DURATION_LIMIT

from helpers.filters import command

from helpers.decorators import errors

from helpers.errors import DurationLimitError

from helpers.gets import get_url, get_file_name

import aiofiles

import ffmpeg

from PIL import Image, ImageFont, ImageDraw

from pytgcalls import StreamType

from pytgcalls.types.input_stream import InputAudioStream

from pytgcalls.types.input_stream import InputStream

def transcode(filename):

    ffmpeg.input(filename).output("input.raw", format='s16le', acodec='pcm_s16le', ac=2, ar='48k').overwrite_output().run() 

    os.remove(filename)

# Convert seconds to mm:ss

def convert_seconds(seconds):

    seconds = seconds % (24 * 3600)

    seconds %= 3600

    minutes = seconds // 60

    seconds %= 60

    return "%02d:%02d" % (minutes, seconds)

# Convert hh:mm:ss to seconds

def time_to_seconds(time):

    stringt = str(time)

    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

# Change image size

def changeImageSize(maxWidth, maxHeight, image):

    widthRatio = maxWidth / image.size[0]

    heightRatio = maxHeight / image.size[1]

    newWidth = int(widthRatio * image.size[0])

    newHeight = int(heightRatio * image.size[1])

    newImage = image.resize((newWidth, newHeight))

    return newImage

async def generate_cover(requested_by, title, views, duration, thumbnail):

    async with aiohttp.ClientSession() as session:

        async with session.get(thumbnail) as resp:

            if resp.status == 200:

                f = await aiofiles.open("background.png", mode="wb")

                await f.write(await resp.read())

                await f.close()

    image1 = Image.open("./background.png")

    image2 = Image.open("etc/foreground.png")

    image3 = changeImageSize(1280, 720, image1)

    image4 = changeImageSize(1280, 720, image2)

    image5 = image3.convert("RGBA")

    image6 = image4.convert("RGBA")

    Image.alpha_composite(image5, image6).save("temp.png")

    img = Image.open("temp.png")

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("etc/font.otf", 32)

    draw.text((190, 550), f"Title: {title}", (255, 255, 255), font=font)

    draw.text(

(190, 590), f"Duration: {duration}", (255, 255, 255), font=font

    )

    draw.text((190, 630), f"Views: {views}", (255, 255, 255), font=font)

    draw.text((190, 670),

 f"Added By: {requested_by}",

 (255, 255, 255),

 font=font,

    )

    img.save("final.png")

    os.remove("temp.png")

    os.remove("background.png")

@Client.on_message(

    command(["play"])

    & filters.group

    & ~filters.edited

    & ~filters.forwarded

    & ~filters.via_bot

)

async def play(_, message: Message):

    global que

    global useer

    lel = await message.reply("🔎 **ഞാൻ 𝐒𝐨𝐧𝐠 🥀 ഒന്നു എടുക്കട്ടേ 🙈 ഒന്നു കാത്തിരിക്കു 🥳.....**") 

    administrators = await get_administrators(message.chat)

    chid = message.chat.id

    try:

        user = await USER.get_me()

    except:

        user.first_name = "Esport_MusicX"

    usar = user

    wew = usar.id

    try:

        await _.get_chat_member(chid, wew)

    except:

        for administrator in administrators:

            if administrator == message.from_user.id:

                try:

                    invitelink = await _.export_chat_invite_link(chid)

                except:

                    await lel.edit(

                        "<b>ആദ്യം 💃🏽എന്നെ ഗ്രൂപ്പിൽ🤩 add അഡ്മിൻ ആക് എന്നിട്ട് 🤝😌പൊളിക്കും നമ്മൾ 💃🏽</b>")

                    return

                try:

                    await USER.join_chat(invitelink)

                    await USER.send_message(

                        message.chat.id, "** ഗയ്‌സ് 😌നമ്മളെ മുത്ത് വന്നു 🔥നിങ്ങൾക് പാടി തരാൻ 🙈**")

                except UserAlreadyParticipant:

                    pass

                except Exception:

                    await lel.edit(

                        f"<b>❰𝐅𝐥𝐨𝐨𝐝 😒 𝐖𝐚𝐢𝐭 𝐄𝐫𝐫𝐨𝐫  😔❱</b>\nഹേയ്, 😍അസിസ്റ്റന്റ് മുത്തേ... 😒 ജോയിൻ ബുദ്ദിമുട്ട് കാരണം നിങ്ങളുടെ ഗ്രൂപ്പിൽ ചേരാനായില്ല ന്റെ കൽബിൻ 😔 ഇനി എന്റെ ഓണർ ഇക്കനോട് ചോദിച്ചു നോക്കി എന്താ പ്രശ്നം എന്ന് 😊𝐇𝐞𝐥𝐩 𝐃𝐦 :- ✨ [❛-𝐌𝐫'MONUUZ💞](https://t.me/Itz_me_monuuz) 💞🥀 :) ")

    try:

        await USER.get_chat(chid)

    except:

        await lel.edit(

            f"<i>Hey {user.first_name}, അസിസ്റ്റന്റ് 🎸 മുത്ത് ഈ 𝐂𝐡𝐚𝐭 ഗ്രൂപ്പിൽ കാണാൻ ഇല്ല ' 𝐀𝐬𝐤 𝐀𝐝𝐦𝐢𝐧 😎 𝐓𝐨 𝐒𝐞𝐧𝐝 /𝐏𝐥𝐚𝐲 ഈ കമെന്റ് ഓക്കേ യൂസ് ആക് 😎 𝐅𝐨𝐫 𝐅𝐢𝐫𝐬𝐭 𝐓𝐢𝐦𝐞 𝐓𝐨 𝐀𝐝𝐝 𝐈𝐭 𝐀𝐧𝐲 𝐇𝐞𝐥𝐩 𝐃𝐦 :- ✨ [❛-༄🦄ᶦᶰᵈ᭄༂❦͟𝑨𝑺𝑯𝑹𝑨𝑭⋆͟ᶜ͟ᴿ͟ᴬ͟ᶻ͟ᴵ͟ᴱ͟ᚸ⃝⃘⃟⃠̰̃ᴷ͟ᵞ͟ᴬ͟ᵀ͟༄༂✰💞▓࿐](https://t.me/itz_me_monuuz) ❤️🥀 </i>")

        return

    

    audio = (

        (message.reply_to_message.audio or message.reply_to_message.voice)

        if message.reply_to_message

        else None

    )

    url = get_url(message)

    if audio:

        if round(audio.duration / 60) > DURATION_LIMIT:

            raise DurationLimitError(

                f"**❰ ° 𝐒𝐨𝐧𝐠 🎸 ° ❱ 𝐋𝐨𝐧𝐠𝐞𝐫 𝐓𝐡𝐚𝐧 {DURATION_LIMIT} 𝐌𝐢𝐧𝐮𝐭𝐞'𝐒 𝐀𝐫𝐞𝐧'𝐭 𝐀𝐥𝐥𝐨𝐰𝐞𝐝 𝐓𝐨 𝐏𝐥𝐚𝐲 ▶ ❤️🥀**"

            )

        file_name = get_file_name(audio)

        title = file_name

        thumb_name = "https://te.legra.ph/file/92dd93f98c61c63c6f100.jpg"

        thumbnail = thumb_name

        duration = round(audio.duration / 60)

        views = "Locally added"

        keyboard = InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                            text="𝐂𝐡𝐚𝐧𝐧𝐞𝐥📡",

                            url=f"https://t.me/cutebabygif916")

               ],

               [

                    InlineKeyboardButton(

                            text="💞❦͟𝑨𝑺𝑯𝑹𝑨𝑭⋆͟",

                            url=f"https://t.me/itz_me_monuuz"),

                            

                    InlineKeyboardButton(

                            text=" 😌yo yo🙈 🥀",

                            url=f"https://t.me/musicstreetgroup")

               ],

               [

                        InlineKeyboardButton(

                            text="𝐆𝐫𝐨𝐮𝐩⭐",

                            url=f"https://t.me/moluuzsupport")

                   

                ]

            ]

        )

        requested_by = message.from_user.first_name

        await generate_cover(requested_by, title, views, duration, thumbnail)

        file_path = await converter.convert(

            (await message.reply_to_message.download(file_name))

            if not path.isfile(path.join("downloads", file_name))

            else file_name

        )

    elif url:

        try:

            results = YoutubeSearch(url, max_results=1).to_dict()

            # print results

            title = results[0]["title"]

            thumbnail = results[0]["thumbnails"][0]

            thumb_name = f"thumb{title}.jpg"

            thumb = requests.get(thumbnail, allow_redirects=True)

            open(thumb_name, "wb").write(thumb.content)

            duration = results[0]["duration"]

            url_suffix = results[0]["url_suffix"]

            views = results[0]["views"]

            durl = url

            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")

            for i in range(len(dur_arr) - 1, -1, -1):

                dur += int(dur_arr[i]) * secmul

                secmul *= 60

            keyboard = InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                            text="𝐂𝐡𝐚𝐧𝐧𝐞𝐥📡",

                            url=f"https://t.me/cutebabygif916")

               ],

               [

                    InlineKeyboardButton(

                            text="💞❦͟𝑨𝑺𝑯𝑹𝑨𝑭⋆͟",

                            url=f"https://t.me/itz_me_monuuz"),

                            

                    InlineKeyboardButton(

                            text=" 😌yo yo🙈 🥀",

                            url=f"https://t.me/musicstreetgroup")

               ],

               [

                        InlineKeyboardButton(

                            text="𝐆𝐫𝐨𝐮𝐩⭐",

                            url=f"https://t.me/moluuzsupport")

                   

                ]

            ]

        )

        except Exception as e:

            title = "NaN"

            thumb_name = "https://te.legra.ph/file/92dd93f98c61c63c6f100.jpg"

            duration = "NaN"

            views = "NaN"

            keyboard = InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                            text="𝐂𝐡𝐚𝐧𝐧𝐞𝐥📡",

                            url=f"https://t.me/cutebabygif916")

               ],

               [

                    InlineKeyboardButton(

                            text="💞❦͟𝑨𝑺𝑯𝑹𝑨𝑭⋆͟",

                            url=f"https://t.me/itz_me_monuuz"),

                            

                    InlineKeyboardButton(

                            text=" 😌yo yo🙈 🥀",

                            url=f"https://t.me/musicstreetgroup")

               ],

               [

                        InlineKeyboardButton(

                            text="𝐆𝐫𝐨𝐮𝐩⭐",

                            url=f"https://t.me/moluuzsupport")

                   

                ]

            ]

        )

        if (dur / 60) > DURATION_LIMIT:

            await lel.edit(

                f"**❰ ° 𝐒𝐨𝐧𝐠 🎸 ° ❱ 𝐋𝐨𝐧𝐠𝐞𝐫 𝐓𝐡𝐚𝐧 {DURATION_LIMIT} 𝐌𝐢𝐧𝐮𝐭𝐞'𝐒 𝐀𝐫𝐞𝐧'𝐭 𝐀𝐥𝐥𝐨𝐰𝐞𝐝 𝐓𝐨 𝐏𝐥𝐚𝐲 ▶ ❤️🥀**"

            )

            return

        requested_by = message.from_user.first_name

        await generate_cover(requested_by, title, views, duration, thumbnail)

        file_path = await converter.convert(youtube.download(url))

    else:

        if len(message.command) < 2:

            return await lel.edit(

                "😍✌ചക്കരെ  നിനക്ക്🎧  ഏത്💞 𝐒𝐨𝐧𝐠 🎸 വേണ്ടത് അത് 𝐏𝐥𝐚𝐲 ▶ 💞 ❤️**"

            )

        await lel.edit("🔎")

        query = message.text.split(None, 1)[1]

        # print(query)

        try:

            results = YoutubeSearch(query, max_results=1).to_dict()

            url = f"https://youtube.com{results[0]['url_suffix']}"

            # print results

            title = results[0]["title"]

            thumbnail = results[0]["thumbnails"][0]

            thumb_name = f"thumb{title}.jpg"

            thumb = requests.get(thumbnail, allow_redirects=True)

            open(thumb_name, "wb").write(thumb.content)

            duration = results[0]["duration"]

            url_suffix = results[0]["url_suffix"]

            views = results[0]["views"]

            durl = url

            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")

            for i in range(len(dur_arr) - 1, -1, -1):

                dur += int(dur_arr[i]) * secmul

                secmul *= 60

        except Exception as e:

            await lel.edit(

                "**🌸° 🥺ടാ മുത്തേ പോന്നുസേ.. എനിക്ക് കിട്ടുന്നില്ലടാ 😔സ്പെല്ലിങ് നോക്കി കറക്റ്റ് അടിക് 🥀.**"

            )

            print(str(e))

            return

        keyboard = InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                            text="𝐂𝐡𝐚𝐧𝐧𝐞𝐥📡",

                            url=f"https://t.me/cutebabygif916")

               ],

               [

                    InlineKeyboardButton(

                            text="💞❦͟𝑨𝑺𝑯𝑹𝑨𝑭⋆͟",

                            url=f"https://t.me/itz_me_monuuz"),

                            

                    InlineKeyboardButton(

                            text=" 😌yo yo🙈 🥀",

                            url=f"https://t.me/musicstreetgroup")

               ],

               [

                        InlineKeyboardButton(

                            text="𝐆𝐫𝐨𝐮𝐩⭐",

                            url=f"https://t.me/moluuzsupport")

                   

                ]

            ]

        )

        if (dur / 60) > DURATION_LIMIT:

            await lel.edit(

                f"**❰ ° 𝐒𝐨𝐧𝐠 🎸 ° ❱ 𝐋𝐨𝐧𝐠𝐞𝐫 𝐓𝐡𝐚𝐧 {DURATION_LIMIT} 𝐌𝐢𝐧𝐮𝐭𝐞'𝐒 𝐀𝐫𝐞𝐧'𝐭 𝐀𝐥𝐥𝐨𝐰𝐞𝐝 𝐓𝐨 𝐏𝐥𝐚𝐲 ▶ ❤️🥀**"

            )

            return

        requested_by = message.from_user.first_name

        await generate_cover(requested_by, title, views, duration, thumbnail)

        file_path = await converter.convert(youtube.download(url))

    ACTV_CALLS = []

    chat_id = message.chat.id

    for x in callsmusic.pytgcalls.active_calls:

        ACTV_CALLS.append(int(x.chat_id))

    if int(chat_id) in ACTV_CALLS:

        position = await queues.put(chat_id, file=file_path)

        await message.reply_photo(

            photo="final.png",

            caption="****💃🏽നിങ്ങൾക് 😂വേണ്ടി സോങ് ഡെഡിക്കേറ്റ് 😍🤝** {}**".format(position),

            reply_markup=keyboard,

        )

    else:

        await callsmusic.pytgcalls.join_group_call(

                chat_id, 

                InputStream(

                    InputAudioStream(

                        file_path,

                    ),

                ),

                stream_type=StreamType().local_stream,

            )

        await message.reply_photo(

            photo="final.png",

            reply_markup=keyboard,

            caption="**അപ്പൊ 😍നമ്മളെ സോങ് മൂഡ് ഇപ്പൊ 🙈 ഗ്രൂപ്പ്‌ 👉  `{}`...**".format(

        message.chat.title

        ), )

    os.remove("final.png")

    return await lel.delete()

    
