import os, time

class Config(object):
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
