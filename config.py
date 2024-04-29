import os, time

class Config(object):
  # database config
    DB_NAME = os.environ.get("DB_NAME","Agsmod")     
    DB_URL  = os.environ.get("DB_URL","")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

class Txt(object):
  PROGRESS_BAR = """\n
╭━━━━❰ᴏɴ ꜰɪʀᴇ 🔥❱━➣
┣⪼ <b>🗃️ Sɪᴢᴇ:</b> {1} | {2}
┣⪼ <b>⏳️ Dᴏɴᴇ :</b> {0}%
┣⪼ <b>🚀 Sᴩᴇᴇᴅ:</b> {3}/s
┣⪼ <b>⏰️ Eᴛᴀ:</b> {4}
╰━━━━━━━━━━━━━━━➣"""
