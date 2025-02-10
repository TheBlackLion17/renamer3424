import os, time

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "22373721")
    API_HASH  = os.environ.get("API_HASH", "6bf8fcaa229c4948941c501a0a5c027c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6041996472:AAECug5QJXvYuKfxf5-nGfC_gUAz_VzZ6OM") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","cluster0")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://king:king@cluster0.mgicw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://envs.sh/Oq2.jpg")
    ADMIN = int(os.environ.get("ADMIN", "5909932224"))
    STRING = os.environ.get("STRING", "BQFVZVkAThwaD5z3Y6BA1qihdkwjNugS00S0Rfcsp5Q6iYIrPv6y8qPcL6d6CkV4T_GEF-4NlFjmo9H8z9aMDsExWvnBL_v9TF6n8F1WthWzD3WqLtwhWjjUMcZuO2nmXe51EwwOI_vxkhYfA_KH1OXmLVYQE3U0uuzze1IVDZvP2mwebpmE-SZA9yceE49RNccpF002dzE3I212Hkn8lwGLyMR9GvD8kQs_lFNi6FGirS0rcPq5IrMzoysaZyv8Lb4illRmJIXbliCU9xQDAE7uV8DuR1mu-kNIaZam5Bs8zq-8hhNM0LZohaWTA9QdQcFwIn_F638PGtq19uxB1JxdZi8XBgAAAAGf1B37AA")

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "AgsModsOG") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002402008837")"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """Halo {}  what's up

𝘐 𝘢𝘮 𝘢 𝘙𝘦𝘯𝘢𝘮𝘦 𝘉𝘰𝘵 
𝘠𝘰𝘶 𝘤𝘢𝘯 𝘶𝘴𝘦 𝘮𝘦 𝘧𝘰𝘳 𝘙𝘦𝘯𝘢𝘮𝘦 & 𝘊𝘩𝘢𝘯𝘨𝘦 𝘛𝘩𝘶𝘮𝘣𝘯𝘢𝘪𝘭 𝘖𝘧 𝘠𝘰𝘶𝘳 𝘍𝘪𝘭𝘦
𝘐 𝘤𝘢𝘯 𝘢𝘭𝘴𝘰 𝘊𝘰𝘯𝘷𝘦𝘳𝘵 𝘝𝘪𝘥𝘦𝘰 𝘛𝘰 𝘍𝘪𝘭𝘦 & 𝘍𝘪𝘭𝘦 𝘛𝘰 𝘝𝘪𝘥𝘦𝘰 

𝘐 𝘸𝘢𝘴 𝘔𝘢𝘥𝘦 𝘉𝘺 : @AgsModsOG"""

    ABOUT_TXT = """
╭───────────────⍟
├<b>🤖 My Name</b> : {}
├<b>🖥️ Developer</b> : <a href=https://t.me/Agsmod>Agsmod Bots</a> 
├<b>👨‍💻 Programer</b> : <a href=https://t.me/Agsmod>Developer</a>
├<b>📕 Library</b> : <a href=https://github.com/pyrogram>Pyrogram</a>
├<b>✏️ Language</b> : <a href=https://www.python.org>Python 3</a>
├<b>💾 Database</b> : <a href=https://cloud.mongodb.com>Mongo DB</a>
├<b>📊 Build Version</b> : <a href=https://t.me/AgsModsOG>Rename v4.5.0</a></b>     
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

✏️ <b><u>How To Rename A File</u></b>

➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].           

𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/Agsmod>Developer</a>
"""

    PROGRESS_BAR = """\n
╭━━━━❰ᴏɴ ꜰɪʀᴇ 🔥❱━➣
┣⪼ <b>🗃️ Sɪᴢᴇ:</b> {1} | {2}
┣⪼ <b>⏳️ Dᴏɴᴇ :</b> {0}%
┣⪼ <b>🚀 Sᴩᴇᴇᴅ:</b> {3}/s
┣⪼ <b>⏰️ Eᴛᴀ:</b> {4}
╰━━━━━━━━━━━━━━━➣"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `8547178698upi@axl`
"""

