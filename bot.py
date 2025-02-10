import asyncio
from pyrogram import Client, compose,idle
import os
from datetime import datetime, timedelta
monitoredSince = datetime.now() 

monitoredSince -= timedelta(seconds=5)

print(monitoredSince)

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6041996472:AAECug5QJXvYuKfxf5-nGfC_gUAz_VzZ6OM")

API_ID = int(os.environ.get("API_ID", "22373721"))

API_HASH = os.environ.get("API_HASH", "6bf8fcaa229c4948941c501a0a5c027c")

STRING = os.environ.get("STRING", "BQFVZVkAThwaD5z3Y6BA1qihdkwjNugS00S0Rfcsp5Q6iYIrPv6y8qPcL6d6CkV4T_GEF-4NlFjmo9H8z9aMDsExWvnBL_v9TF6n8F1WthWzD3WqLtwhWjjUMcZuO2nmXe51EwwOI_vxkhYfA_KH1OXmLVYQE3U0uuzze1IVDZvP2mwebpmE-SZA9yceE49RNccpF002dzE3I212Hkn8lwGLyMR9GvD8kQs_lFNi6FGirS0rcPq5IrMzoysaZyv8Lb4illRmJIXbliCU9xQDAE7uV8DuR1mu-kNIaZam5Bs8zq-8hhNM0LZohaWTA9QdQcFwIn_F638PGtq19uxB1JxdZi8XBgAAAAGf1B37AA")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
