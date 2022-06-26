import logging, os, random
from pyrogram import filters, Client, __version__ as pyro
from pyrogram.types import *
import time
import requests 

# enable logging
FORMAT = "[Nekos-Best-Bot] %(message)s"
logging.basicConfig(
    level=logging.INFO, format=FORMAT
)
  

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
SUPPORT = os.environ.get("SUPPORT", None)
UPDATES = os.environ.get("UPDATES", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None) 


bot = Client("nandhabot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


buttons = [
    [
        InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton("Onii Chan", url=f"https://t.me/Lord_DSP_3"),
        InlineKeyboardButton("Schwi𝄞", url=f"https://t.me/Schwi_Musicbot"),
    ],
    [
        InlineKeyboardButton("ANIME CHAT ?", url=f"https://t.me/+LuNfF7pzIggyNWE1"),
    ],
 ]

PM_START_TEXT = """Hey there!
I'm Izumi Sagiri 💞

I only work for 𓆩⌬𓆪 UCO
@UNITED_COMMUNITY_OF_OTAKUS 
⁄(⁄ ⁄•⁄-⁄•⁄ ⁄)⁄
"""

RANDOM = [
    "https://telegra.ph/file/ae3cef2e017f42d7e1a68.jpg",
    "https://telegra.ph/file/75dc19a42641f145ed17d.jpg",
    "https://telegra.ph/file/8ab286d88face56230dc2.jpg",
    "https://telegra.ph/file/f5c0ff5e049e6d6f08ba5.jpg",
    "https://telegra.ph/file/e03ebae8b3141206b8155.jpg",
    "https://telegra.ph/file/9ebcc67b6f725e74c0db2.jpg",
    "https://telegra.ph/file/6c83cbacbf445faefd3dd.jpg",
    "https://telegra.ph/file/b90b411cbddf9c117d7ff.jpg",
    "https://telegra.ph/file/baec0c09beeb51ae34dc9.jpg",
    "https://telegra.ph/file/6c1503f2160912be2b506.jpg",
    "https://telegra.ph/file/cb266ed8173fee64f8816.jpg",
    "https://telegra.ph/file/cd54645e7f572e8f09fa9.jpg",
    "https://telegra.ph/file/07d530ab8e2afb9d102df.jpg",
    "https://telegra.ph/file/3df641544655a210b3490.jpg",
    "https://telegra.ph/file/7d05845c20c8dca63aac0.jpg",
    "https://telegra.ph/file/a830abb333c66ed0fd180.jpg",
    "https://telegra.ph/file/ee7cd0fe6cc759212f484.jpg",
    "https://telegra.ph/file/aa2902e30756c1654c677.jpg",
    "https://telegra.ph/file/e0ed8785ddee4b26780af.jpg",
    "https://telegra.ph/file/95707b6057fc4eb536c23.jpg",
    "https://telegra.ph/file/f7cbc1343497bd5b7c3ea.jpg",
    "https://telegra.ph/file/32eae8c785c820e0c82e7.jpg",
    "https://telegra.ph/file/230a2ed603e5de3db1c51.jpg",
    "https://telegra.ph/file/5195a5000b712f8340ed5.jpg",
    "https://telegra.ph/file/20588d51d672ba93416c4.jpg",
    "https://telegra.ph/file/d085269311820f5f0ecec.jpg",
    "https://telegra.ph/file/790dfc57e28a167d11ae2.jpg",
    "https://telegra.ph/file/6819ccad4f4dc79beca6e.mp4",
    "https://telegra.ph/file/0e0b7d5992385009f281d.jpg",
    "https://telegra.ph/file/c5a50dc9cf1423c49a73d.mp4"
    "https://telegra.ph/file/d2a12267581a73844e547.jpg",
    "https://telegra.ph/file/a56b67316503f4557208f.jpg",
    "https://telegra.ph/file/60dfafcf53695bb456d1f.jpg",
    "https://telegra.ph/file/c836f56c1368cf8bcf270.jpg",
    "https://telegra.ph/file/a06f3120ff84d4b94c656.jpg",
    "https://telegra.ph/file/e620b8d8d3511306eeee5.jpg",
    "https://telegra.ph/file/9460dc81d9f340b4869c6.jpg",
    "https://telegra.ph/file/a7b52830a0be42fe44469.jpg",
    "https://telegra.ph/file/a8ce4b59a9cdf61d5dcc4.jpg",
    "https://telegra.ph/file/6c3882f915c019151d8d2.jpg",
    "https://telegra.ph/file/69ef629540ef8fd38d6da.jpg",
    "https://telegra.ph/file/0922ffab1ebfae1d54b2e.jpg",
    "https://telegra.ph/file/b84d010ad66563f4f7d83.jpg",
    "https://telegra.ph/file/a5757edcdb95c9934bca1.jpg",
    "https://telegra.ph/file/81aa75ed5b0d60eedc596.jpg",
    "https://telegra.ph/file/9047c6ecc447c6d164672.jpg",
    "https://telegra.ph/file/8697d90e8f9a1d4b96045.jpg",
    "https://telegra.ph/file/96ffc81f38a03f840e1f4.jpg",
    "https://telegra.ph/file/73cd996c153b8e5b48daa.jpg",
    "https://telegra.ph/file/38e9ba4d318202f12b016.jpg",
    "https://telegra.ph/file/ea6c2a06d678ee052ef16.jpg",
    "https://telegra.ph/file/e3b3eee1b9685bd659005.jpg",
    "https://telegra.ph/file/cd921994f219a807505ca.jpg",
    "https://telegra.ph/file/e1f5e942f5687d6ac8ae2.jpg",
    "https://telegra.ph/file/a46d4a281fba0fdfa081b.jpg",
    "https://telegra.ph/file/76b46ab043d9b37b126f1.jpg",
    "https://telegra.ph/file/5fa82f5e4cc07d1ae2436.jpg",
    "https://telegra.ph/file/a5a03c942dcd1774d2058.jpg",
    "https://telegra.ph/file/91d36bcb96e9ced8f1465.jpg",
    "https://telegra.ph/file/727aa116f6300eee9dba1.jpg",
    "https://telegra.ph/file/9e5ca6c0543d530ff4728.jpg",
    "https://telegra.ph/file/926fc4a67e720e8498e1b.jpg",
    "https://telegra.ph/file/086d5eaf3a65791d73110.jpg",
    "https://telegra.ph/file/391cee04c0bf3b064aebe.jpg",
    "https://telegra.ph/file/263fc9dea6dda28216c17.jpg",
    "https://telegra.ph/file/75a027ab77798c3f641c6.jpg",
    "https://telegra.ph/file/0e0b7d5992385009f281d.jpg",
]

MALENEKO = [
    "https://telegra.ph/file/dee6bb78f44e4c6984acb.jpg",
    "https://telegra.ph/file/56c3292abaf8b7d4bd52f.jpg",
    "https://telegra.ph/file/d3e7ef3734039b5968fa4.jpg",
    "https://telegra.ph/file/4737f8426eb74742da149.jpg",
    "https://telegra.ph/file/f70c6a17344569a150543.jpg",
    "https://telegra.ph/file/803ad8d1925b2dfd53f2a.jpg",
    "https://telegra.ph/file/c75608abd53e56800c619.jpg",
    "https://telegra.ph/file/9f4d71e644c7988be4123.jpg",
    "https://telegra.ph/file/f913d0439ac4ee4ec0380.jpg",
    "https://telegra.ph/file/32b74701bac5db4c9ff9f.jpg",
    "https://telegra.ph/file/3a347fc12b9696b735cb6.jpg",
    "https://telegra.ph/file/6c57c3c79df6f2714c645.jpg",
    "https://telegra.ph/file/b1193a34f84faf82efca8.jpg",
    "https://telegra.ph/file/3f95c6e8ccf15b67d4574.jpg",
    "https://telegra.ph/file/cd1c1f7b8d2e8cb3461eb.jpg",
    "https://telegra.ph/file/e143af6cfd3dff4aa4910.jpg",

]


@bot.on_message(filters.command(["start","help"])& filters.private)
async def start(_, m):
       image = random.choice(RANDOM)
       await m.reply_photo(photo=image, caption=PM_START_TEXT.format(m.from_user.mention),
             reply_markup=InlineKeyboardMarkup(buttons))

HELP_TEXT = """
**Anime Themed SFW:**

💓 /pat : To Pat A Person
💓 /hug : To Hug A Person
💓 /kiss : To Kiss A Person
💓 /slap : To Slap A Person
💓 /feed : To Feed A Person
💓 /bite : To Bite A Person
💓 /poke : To Poke A Person
💓 /cry : Shows you Cried
💓 /laugh : Shows you're Laughing
💓 /tickle : To Tickle A Person
💓 /cuddle : To Cuddle A Person
💓 /baka : To Say A Person Baka

**Hit the More button below to explore more Cammands ^_^**
"""

@bot.on_callback_query(filters.regex("help_back"))
async def helpback(_, query: CallbackQuery):
           query = query.message
           await query.edit_caption(HELP_TEXT,
             reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴍᴏʀᴇ❓", callback_data="more_help_text"),
                InlineKeyboardButton("Try ❔", url=f"https://t.me/+LuNfF7pzIggyNWE1")]]))


ABOUT_TEXT = """
╔═════(༻❛☉❟༺)═════╗
╟𝙑𝙚𝙧𝙨𝙞𝙤𝙣⌱ 7.D3
╟𝙈𝙖𝙙𝙚 𝙗𝙮⌱『𝓛𝓸𝓻𝓭 𝕯𝕾𝕻 𝟑 』
╟𓆩⌬𓆪 𝙐𝘾𝙊⌱ @A_inviteLink
╟𝙀𝙧𝙧𝙤𝙧? ⌱ @UCO404bot
╟𝘾𝙝𝙚𝙘𝙠𝙤𝙪𝙩 ⌱ @C2_Probot
╟𝘾𝙝𝙚𝙘𝙠𝙤𝙪𝙩 ⌱ @Schwi_Musicbot
╚═════(༻❛☉❟༺)═════╝
"""

@bot.on_callback_query(filters.regex("about_back"))
async def about(_, query: CallbackQuery):
           query = query.message
           await query.edit_caption(ABOUT_TEXT.format(pyro),
             reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="help_back")]]))

MORE_HELP_TEXT = """
**Try and know <(￣︶￣)↗**

💗 /pout  :  To Pout
💗 /wink  :  To Wink
💗 /smile : To Smile
💗 /blush : To Blush
🍀 /smug  : To Smug To A Person
🍀 /happy : To Show you're Happy
🍀 /stare : To Stare At A Person
🍀 /dance : To Dance With Anyone
🎐 /shrug : To Shrug A Person
🎐 /think : To Show You're Thinking
🎐 /bored : To Show You're Bored Rn
🎐 /sleep : To Show You're Sleepy
🎗️ /highfive : To Highfive A Person
🎗️ /thumbsup : To Thumbsup A Person
🎗️ /wave     : To Wave Hand To A Person
🎗️ /facepalm : To Makes A Person Facepalm

🥀 /cute :  To Say Me Cute
🥀 /waifu : To Send Random Waifu Image
🐱 /nekogirl : To Get Random Cat girls wall.
😼 /nekoboy  : To Get Random Cat boys wall.
👘 /kitsune : To Send Random Kitsune Image
"""
@bot.on_callback_query(filters.regex("more_help_text"))
async def helpmore(_, query: CallbackQuery):
           query = query.message
           await query.edit_caption(MORE_HELP_TEXT,
             reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="help_back")]]))


OWO = (
    "*Izumi pats {} on the head.",
    "*gently rubs {}'s head*.",
    "*Izumi mofumofus {}'s head*",
    "*Izumi messes up {}'s head*",
    "*Izumi intensly rubs {}'s head*",
    "*{}'s waifu pats their head*",
    "*{}'s got free headpats*",
    "No pats for {}!",
)

neko_text = (
 "(*)^(*) *lazy arrival* zzzZZ(Z){}-kun I'm hungry...",
 "OwO why are calling me *wags tail in excitement* {} Do you have have cookies?",
 "^~^ *peeks by wall* Oh! {} Meowwww",
 "Ara Ara! {} Do you wanna play? *raises cat ears* ^attentive^",
 "($^$) *money face* {} are you rich UwU?",
 "Hello UwU {} I'm here to play, Meow"
)


@bot.on_message(filters.command("kiss")& filters.group)
async def kiss(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/kiss"
       r = requests.get(url)
       e = r.json()
       kissme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(kissme, caption="{}  kisses  {}".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/kiss"
      r = requests.get(url)
      e = r.json()
      kissme = e["results"][0]["url"]
      await message.reply_video(kissme, caption="Kisses u with all my love~")
      return

@bot.on_message(filters.command("highfive")& filters.group)
async def highfive(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/highfive"
       r = requests.get(url)
       e = r.json()
       highfiveme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(highfiveme, caption="{} gave highfives to {}".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/highfive"
      r = requests.get(url)
      e = r.json()
      highfiveme = e["results"][0]["url"]
      await message.reply_video(highfiveme, caption="Highfives U With All My Friendship~")
      return

@bot.on_message(filters.command("happy")& filters.group)
async def happy(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/happy"
       r = requests.get(url)
       e = r.json()
       happyme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(happyme, caption="{}  Is Happy for  {}".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/happy"
      r = requests.get(url)
      e = r.json()
      happyme = e["results"][0]["url"]
      await message.reply_video(happyme)
      return

@bot.on_message(filters.command("laugh")& filters.group)
async def laugh(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/laugh"
       r = requests.get(url)
       e = r.json()
       laughme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(laughme, caption="{} Is Laughing to {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/laugh"
      r = requests.get(url)
      e = r.json()
      laughme = e["results"][0]["url"]
      await message.reply_video(laughme)
      return

@bot.on_message(filters.command("bite")& filters.group)
async def bite(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/bite"
       r = requests.get(url)
       e = r.json()
       biteme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(biteme, caption="{}   Bites   {}".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/bite"
      r = requests.get(url)
      e = r.json()
      biteme = e["results"][0]["url"]
      await message.reply_video(biteme, caption="Gently bites you! nya!")
      return

@bot.on_message(filters.command("poke")& filters.group)
async def poke(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/poke"
       r = requests.get(url)
       e = r.json()
       pokeme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(pokeme, caption="{}   pokes   {}".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/poke"
      r = requests.get(url)
      e = r.json()
      pokeme = e["results"][0]["url"]
      await message.reply_video(pokeme, caption="*Poking You Continuously*")
      return

@bot.on_message(filters.command("tickle")& filters.group)
async def tickle(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/tickle"
       r = requests.get(url)
       e = r.json()
       tickleme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(tickleme, caption="{}  tickles  {}".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/tickle"
      r = requests.get(url)
      e = r.json()
      tickleme = e["results"][0]["url"]
      await message.reply_video(tickleme, caption="*Tickling You Continuously*")
      return

@bot.on_message(filters.command("wave")& filters.group)
async def wave(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/wave"
       r = requests.get(url)
       e = r.json()
       waveme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(waveme, caption="{}  waves  {}".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/wave"
      r = requests.get(url)
      e = r.json()
      waveme = e["results"][0]["url"]
      await message.reply_video(waveme, caption="*My Hand Waving To You*~")
      return

@bot.on_message(filters.command("thumbsup")& filters.group)
async def thumbsup(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/thumbsup"
       r = requests.get(url)
       e = r.json()
       thumbsupme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(thumbsupme, caption="{} thumbsups to {}".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/thumbsup"
      r = requests.get(url)
      e = r.json()
      thumbsupme = e["results"][0]["url"]
      await message.reply_video(thumbsupme, caption="👍🏻✨💞")
      return

@bot.on_message(filters.command("stare")& filters.group)
async def stare(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/stare"
       r = requests.get(url)
       e = r.json()
       stareme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(stareme, caption="{}  staring at  {}".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/stare"
      r = requests.get(url)
      e = r.json()
      stareme = e["results"][0]["url"]
      await message.reply_video(stareme, caption="👀!?")
      return

@bot.on_message(filters.command("cuddle")& filters.group)
async def cuddle(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/cuddle"
       r = requests.get(url)
       e = r.json()
       cuddleme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(cuddleme, caption="{} cuddles {}".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/cuddle"
      r = requests.get(url)
      e = r.json()
      cuddleme = e["results"][0]["url"]
      await message.reply_video(cuddleme, caption="Cuddle you with all my love")
      return

@bot.on_message(filters.command("smile")& filters.group)
async def smile(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/smile"
       r = requests.get(url)
       e = r.json()
       smileme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(smileme, caption="{} smiled to {}".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/smile"
      r = requests.get(url)
      e = r.json()
      smileme = e["results"][0]["url"]
      await message.reply_video(smileme)
      return

@bot.on_message(filters.command("baka")& filters.group)
async def baka(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/baka"
       r = requests.get(url)
       e = r.json()
       bakame = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(bakame, caption="{} said {} is baka!".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/baka"
      r = requests.get(url)
      e = r.json()
      bakame = e["results"][0]["url"]
      await message.reply_video(video=f"https://telegra.ph/file/09a7357b0f0b3975ccd81.mp4", caption="BAKAAAA!!!!")
      return

@bot.on_message(filters.command("blush")& filters.group)
async def blush(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/blush"
       r = requests.get(url)
       e = r.json()
       blushme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(blushme, caption="{} blushes to {}".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/blush"
      r = requests.get(url)
      e = r.json()
      blushme = e["results"][0]["url"]
      name1 = message.from_user.mention
      await message.reply_video(blushme, caption="{} is blused!".format(name1))
      return

@bot.on_message(filters.command("think")& filters.group)
async def think(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/think"
       r = requests.get(url)
       e = r.json()
       thinkme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(thinkme, caption="{} is thinking what to say to {}".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/think"
      r = requests.get(url)
      e = r.json()
      thinkme = e["results"][0]["url"]
      name = message.from_user.mention
      await message.reply_video(thinkme, caption="{} is in deep thoughts....".format(name))
      return

@bot.on_message(filters.command("pout")& filters.group)
async def pout(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/pout"
       r = requests.get(url)
       e = r.json()
       poutme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(poutme, caption="{}  pouts to {}".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/pout"
      r = requests.get(url)
      e = r.json()
      name = message.from_user.mention
      poutme = e["results"][0]["url"]
      await message.reply_video(poutme, caption="~{}~".format(name))
      return

@bot.on_message(filters.command("facepalm")& filters.group)
async def facepalm(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/facepalm"
       r = requests.get(url)
       e = r.json()
       facepalmme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(facepalmme, caption="{} Made {} To Facepalm ".format(name2, name1))
       return
    else:
      url = "https://nekos.best/api/v2/facepalm"
      r = requests.get(url)
      e = r.json()
      name = message.from_user.first_name
      facepalmme = e["results"][0]["url"]
      await message.reply_video(facepalmme)
      return

@bot.on_message(filters.command("wink")& filters.group)
async def wink(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/wink"
       r = requests.get(url)
       e = r.json()
       winkme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(winkme, caption="{}  winks  {}".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/wink"
      r = requests.get(url)
      e = r.json()
      winkme = e["results"][0]["url"]
      await message.reply_video(winkme, caption="Winks u with all my love~")
      return

@bot.on_message(filters.command("smug")& filters.group)
async def smug(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/smug"
       r = requests.get(url)
       e = r.json()
       smugme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(smugme, caption="{} sumgs to {}".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/smug"
      r = requests.get(url)
      e = r.json()
      smugme = e["results"][0]["url"]
      await message.reply_video(smugme, caption="*Hehehehehehehehe*~")
      return

@bot.on_message(filters.command("cry")& filters.group)
async def cry(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/cry"
       r = requests.get(url)
       e = r.json()
       cryme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(cryme, caption="{} made {} Cry.".format(name2, name1))
       return
    else:
      url = "https://nekos.best/api/v2/cry"
      r = requests.get(url)
      e = r.json()
      cryme = e["results"][0]["url"]
      await message.reply_video(cryme)
      return

@bot.on_message(filters.command("dance")& filters.group)
async def dance(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/dance"
       r = requests.get(url)
       e = r.json()
       danceme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(danceme, caption="*{} grabs {} to dance together!".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/dance"
      r = requests.get(url)
      e = r.json()
      name = message.from_user.mention
      danceme = e["results"][0]["url"]
      await message.reply_video(danceme)
      return

@bot.on_message(filters.command("feed")& filters.group)
async def feed(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/feed"
       r = requests.get(url)
       e = r.json()
       feedme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(feedme, caption="{}  feeds  {}".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/feed"
      r = requests.get(url)
      e = r.json()
      feedme = e["results"][0]["url"]
      name = message.from_user.mention
      await message.reply_video(feedme, caption="Say Aaaaaa {}".format(name))
      return

@bot.on_message(filters.command("shrug")& filters.group)
async def shrug(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/shrug"
       r = requests.get(url)
       e = r.json()
       shrugme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(shrugme, caption="{} shrugs to {}".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/shrug"
      r = requests.get(url)
      e = r.json()
      name = message.from_user.mention
      shrugme = e["results"][0]["url"]
      await message.reply_video(shrugme, caption="Nani! the what!?".format(name))
      return

@bot.on_message(filters.command("bored")& filters.group)
async def bored(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/bored"
       r = requests.get(url)
       e = r.json()
       boredme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       await message.reply_to_message.reply_video(boredme, caption="*{} is bored...".format(name1))
       return
    else:
      url = "https://nekos.best/api/v2/bored"
      r = requests.get(url)
      e = r.json()
      name = message.from_user.mention
      boredme = e["results"][0]["url"]
      await message.reply_video(boredme, caption="*{} is so bored rn....".format(name))
      return


@bot.on_message(filters.command("pat")& filters.group)
def pat(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/pat"
       r = requests.get(url)
       e = r.json()
       patme = e["results"][0]["url"]
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       message.reply_to_message.reply_video(patme, caption="{}  pats  {}".format(name1, name2))
    else:    
      name = (
          message.reply_to_message.from_user.mention
          if message.reply_to_message
          else message.from_user.first_name
      )
      url = "https://nekos.best/api/v2/pat"
      r = requests.get(url)
      e = r.json()
      patme = e["results"][0]["url"]
      message.reply_video(patme, caption=random.choice(OWO).format(name))

@bot.on_message(filters.command("hug")& filters.group)
def hug(_, message):
    
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/hug"
       r = requests.get(url)
       e = r.json()
       hugme = e["results"][0]["url"]
       
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       message.reply_to_message.reply_video(hugme, caption="{}  hugs  {}".format(name1, name2))
    else:
       url = "https://nekos.best/api/v2/hug"
       r = requests.get(url)
       e = r.json()
       hugme = e["results"][0]["url"]
       
       message.reply_video(hugme, caption="*Hugs u with all my love*")

@bot.on_message(filters.command("slap")& filters.group)      
def slap(_, message):
    
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/slap"
       r = requests.get(url)
       e = r.json()
       slapme = e["results"][0]["url"]
       
       name1 = message.from_user.mention
       name2 = message.reply_to_message.from_user.mention
       message.reply_to_message.reply_video(slapme, caption="{}  slaps  {}".format(name1, name2))
    else:
       url = "https://nekos.best/api/v2/slap"
       r = requests.get(url)
       e = r.json()
       slapme = e["results"][0]["url"]
       
       message.reply_video(slapme, caption="Take this!")

@bot.on_message(filters.command("cute")& filters.group)
def cute(_, message):
    name = message.from_user.mention         
    url = f"https://nekos.best/api/v2/neko"
    r = requests.get(url)
    e = r.json()
    cuteme = e["results"][0]["url"]
    message.reply_photo(
        cuteme, caption="Thank UwU {}  *smiles and hides*".format(name)
    )

@bot.on_message(filters.command("waifu")& filters.group)
def waifu(_, message):
    name = message.from_user.first_name         
    url = f"https://nekos.best/api/v2/waifu"
    r = requests.get(url)
    e = r.json()
    waifume = e["results"][0]["url"]
    message.reply_photo(
        waifume, caption="Waifu for {}".format(name)
    )

@bot.on_message(filters.command("kitsune")& filters.group)
def kitsune(_, message):
    name = message.from_user.first_name         
    url = f"https://nekos.best/api/v2/kitsune"
    r = requests.get(url)
    e = r.json()
    kitsuneme = e["results"][0]["url"]
    message.reply_photo(kitsuneme)



@bot.on_message(filters.command("sleep")& filters.group)
def sleep(_, message):
    sleep_type = random.choice(("Text", "Gif", "Video"))
    if sleep_type == "Gif":
        try:
            url = "https://nekos.best/api/v2/sleep"
            r = requests.get(url)
            e = r.json()
            sleepme = e["results"][0]["url"]
            message.reply_video(sleepme)
        except BadRequest:
            sleep_type = "Text"

    if sleep_type == "Video":
        try:
            bed = "https://telegra.ph/file/0263c22ac828d68174465.mp4"
            message.reply_video(bed)
        except BadRequest:
            sleep_type = "Text"

    if sleep_type == "Text":
        z = ". . . (∪｡∪)｡｡｡zzzZZ"
        message.reply_text(z)

@bot.on_message(filters.command("nekogirl")& filters.group)
def nekogirl(_, message):
    url = "https://nekos.best/api/v2/neko"
    r = requests.get(url)
    e = r.json()
    NEKO_IMG = e["results"][0]["url"]
    name = message.from_user.mention
    ke = random.choice(neko_text)
    message.reply_photo(photo=NEKO_IMG, caption=ke.format(name))

@bot.on_message(filters.command("nekoboy")& filters.group)
def nekoboy(_, message):
    image = random.choice(MALENEKO)
    name = message.from_user.mention
    ke = random.choice(neko_text)
    message.reply_photo(photo=image, caption=ke.format(name))

@bot.on_message(filters.command(["ping"])) 
async def ping(_, message: Message):
    image = random.choice(RANDOM)
    await message.reply_photo(photo=image, caption=f"💖🤍92.935 ms🤍💖")

@bot.on_message(filters.command(["start"])& filters.group)
async def on_start(_, message: Message):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🤍 Help Section 🤍",
                    url=f"https://t.me/Sagiri_izumi_Robot?start=help",
                ),
            ]
        ]
    )
    image = random.choice(RANDOM)
    send = await message.reply_photo(image, caption=f"Start me in DM.", reply_markup=upl)

    
bot.run()
with bot:
         bot.send_message(f"@{SUPPORT}", f"Hello there I'm Online!\nPyroVersion: {pyro}")
