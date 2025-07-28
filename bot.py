import logging
import logging.config
from pyrogram import Client
from aiohttp import web
from config import Config
from plugins.web_support import web_server

# ─── Logging Configuration ─────────────────────────────────────────────────────

logging.config.fileConfig('logging.conf')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# ─── Bot Client Definition ─────────────────────────────────────────────────────

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            sleep_threshold=5,
            plugins={"root": "plugins"},
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username
        self.force_channel = FORCE_SUB

        # Force Subscription Invite Link
        if self.force_channel:
            try:
                invite_link = await self.export_chat_invite_link(self.force_channel)
                self.invitelink = invite_link
            except Exception as e:
                logger.warning("❗ Force Sub Error: %s", e)
                logger.warning("⚠️ Make sure the bot is admin in FORCE_SUB channel.")
                self.force_channel = None

        # Start Web Server (for health check / render)
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", PORT).start()

        logger.info(f"✅ Bot @{self.username} started successfully!")

    async def stop(self, *args):
        await super().stop()
        logger.info("🛑 Bot Stopped")


# ─── Entry Point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    bot = Bot()
    bot.run()
