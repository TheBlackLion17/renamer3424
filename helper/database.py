import motor.motor_asyncio
from config import Config
from .utils import send_log

class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db["user"]

    def new_user(self, id):
        return {
            "_id": int(id),
            "file_id": None,
            "caption": None,
            "prefix": None,
            "suffix": None,
        }

    async def add_user(self, bot, message):
        user = message.from_user
        if not await self.is_user_exist(user.id):
            new_user = self.new_user(user.id)
            await self.col.insert_one(new_user)
            await send_log(bot, user)

    async def is_user_exist(self, id):
        user = await self.col.find_one({"_id": int(id)})
        return bool(user)

    async def total_users_count(self):
        return await self.col.count_documents({})

    async def get_all_users(self):
        return self.col.find({})

    async def delete_user(self, user_id):
        await self.col.delete_many({"_id": int(user_id)})

    async def set_thumbnail(self, id, file_id):
        await self.col.update_one({"_id": int(id)}, {"$set": {"file_id": file_id}})

    async def get_thumbnail(self, id):
        user = await self.col.find_one({"_id": int(id)})
        return user.get("file_id") if user else None

    async def set_caption(self, id, caption):
        await self.col.update_one({"_id": int(id)}, {"$set": {"caption": caption}})

    async def get_caption(self, id):
        user = await self.col.find_one({"_id": int(id)})
        return user.get("caption") if user else None

    async def set_prefix(self, id, prefix):
        await self.col.update_one({"_id": int(id)}, {"$set": {"prefix": prefix}})

    async def get_prefix(self, id):
        user = await self.col.find_one({"_id": int(id)})
        return user.get("prefix") if user else None

    async def set_suffix(self, id, suffix):
        await self.col.update_one({"_id": int(id)}, {"$set": {"suffix": suffix}})

    async def get_suffix(self, id):
        user = await self.col.find_one({"_id": int(id)})
        return user.get("suffix") if user else None


# Initialize the database connection
agsbots = Database(Config.DB_URL, Config.DB_NAME)
