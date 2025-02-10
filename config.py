import os, time

class Config(object):

TOKEN = os.environ.get("TOKEN", "6041996472:AAECug5QJXvYuKfxf5-nGfC_gUAz_VzZ6OM")

API_ID = int(os.environ.get("API_ID", "22373721"))

API_HASH = os.environ.get("API_HASH", "6bf8fcaa229c4948941c501a0a5c027c")

STRING = os.environ.get("STRING", "BQFVZVkAThwaD5z3Y6BA1qihdkwjNugS00S0Rfcsp5Q6iYIrPv6y8qPcL6d6CkV4T_GEF-4NlFjmo9H8z9aMDsExWvnBL_v9TF6n8F1WthWzD3WqLtwhWjjUMcZuO2nmXe51EwwOI_vxkhYfA_KH1OXmLVYQE3U0uuzze1IVDZvP2mwebpmE-SZA9yceE49RNccpF002dzE3I212Hkn8lwGLyMR9GvD8kQs_lFNi6FGirS0rcPq5IrMzoysaZyv8Lb4illRmJIXbliCU9xQDAE7uV8DuR1mu-kNIaZam5Bs8zq-8hhNM0LZohaWTA9QdQcFwIn_F638PGtq19uxB1JxdZi8XBgAAAAGf1B37AA")

ADMIN = os.environ.get("ADMIN", "5909932224")

  # database config
    DB_NAME = os.environ.get("DB_NAME","cluster0")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://king:king@cluster0.mgicw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002402008837"))

class Txt(object):
  PROGRESS_BAR = """\n
╭━━━━❰ᴏɴ ꜰɪʀᴇ 🔥❱━➣
┣⪼ <b>🗃️ Sɪᴢᴇ:</b> {1} | {2}
┣⪼ <b>⏳️ Dᴏɴᴇ :</b> {0}%
┣⪼ <b>🚀 Sᴩᴇᴇᴅ:</b> {3}/s
┣⪼ <b>⏰️ Eᴛᴀ:</b> {4}
╰━━━━━━━━━━━━━━━➣"""
