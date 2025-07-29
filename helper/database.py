import motor.motor_asyncio
from config import Config
from .utils import send_log
from pyrogram import Client
from pyrogram.types import Message


class Database:
    def __init__(self, uri: str, database_name: str):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db["user"]

    def uploadlimit(chat_id, limit):
    dbcol.update_one({"_id": chat_id}, {"$set": {"uploadlimit": limit}})


def addpre(chat_id):
    date = add_date()
    dbcol.update_one({"_id": chat_id}, {"$set": {"prexdate": date[0]}})


def addpredata(chat_id):
    dbcol.update_one({"_id": chat_id}, {"$set": {"prexdate": None}})


def daily(chat_id, date):
    dbcol.update_one({"_id": chat_id}, {"$set": {"daily": date}})


    def new_user(self, user_id: int) -> dict:
        return {
            "_id": user_id,
            "file_id": None,
            "caption": None,
            "prefix": None,
            "suffix": None,
            "uploadlimit": 2147483648,  # Default 2GB
            "usertype": "Free"
        }

    async def init_indexes(self):
        try:
            await self.col.create_index([("_id", 1)], unique=True)
        except Exception as e:
            print(f"Index creation failed: {e}")

    async def add_user(self, bot: Client, message: Message) -> None:
        try:
            user = message.from_user
            if not await self.is_user_exist(user.id):
                new_user = self.new_user(user.id)
                await self.col.insert_one(new_user)
                await send_log(bot, user)
        except Exception as e:
            print(f"Error adding user: {e}")

    async def is_user_exist(self, user_id: int) -> bool:
        try:
            user = await self.col.find_one({"_id": user_id})
            return bool(user)
        except Exception as e:
            print(f"Error checking user existence: {e}")
            return False

    async def total_users_count(self) -> int:
        try:
            return await self.col.count_documents({})
        except Exception as e:
            print(f"Error counting users: {e}")
            return 0

    async def get_all_users(self) -> list:
        try:
            return [user async for user in self.col.find({})]
        except Exception as e:
            print(f"Error fetching all users: {e}")
            return []

    async def delete_user(self, user_id: int) -> None:
        try:
            await self.col.delete_many({"_id": user_id})
        except Exception as e:
            print(f"Error deleting user: {e}")

    async def delete_all_users(self) -> None:
        try:
            await self.col.delete_many({})
        except Exception as e:
            print(f"Error clearing user database: {e}")

    async def set_thumbnail(self, user_id: int, file_id: str) -> None:
        try:
            await self.col.update_one({"_id": user_id}, {"$set": {"file_id": file_id}})
        except Exception as e:
            print(f"Error setting thumbnail: {e}")

    async def get_thumbnail(self, user_id: int) -> str | None:
        try:
            user = await self.col.find_one({"_id": user_id})
            return user.get("file_id") if user else None
        except Exception as e:
            print(f"Error getting thumbnail: {e}")
            return None

    async def set_caption(self, user_id: int, caption: str) -> None:
        try:
            await self.col.update_one({"_id": user_id}, {"$set": {"caption": caption}})
        except Exception as e:
            print(f"Error setting caption: {e}")

    async def get_caption(self, user_id: int) -> str | None:
        try:
            user = await self.col.find_one({"_id": user_id})
            return user.get("caption") if user else None
        except Exception as e:
            print(f"Error getting caption: {e}")
            return None

    async def set_prefix(self, user_id: int, prefix: str) -> None:
        try:
            await self.col.update_one({"_id": user_id}, {"$set": {"prefix": prefix}})
        except Exception as e:
            print(f"Error setting prefix: {e}")

    async def get_prefix(self, user_id: int) -> str | None:
        try:
            user = await self.col.find_one({"_id": user_id})
            return user.get("prefix") if user else None
        except Exception as e:
            print(f"Error getting prefix: {e}")
            return None

    async def set_suffix(self, user_id: int, suffix: str) -> None:
        try:
            await self.col.update_one({"_id": user_id}, {"$set": {"suffix": suffix}})
        except Exception as e:
            print(f"Error setting suffix: {e}")

    async def get_suffix(self, user_id: int) -> str | None:
        try:
            user = await self.col.find_one({"_id": user_id})
            return user.get("suffix") if user else None
        except Exception as e:
            print(f"Error getting suffix: {e}")
            return None

    # 🔒 Premium Upload Limit
    async def uploadlimit(self, user_id: int) -> int:
        user = await self.col.find_one({"_id": user_id})
        return user.get("uploadlimit", 2147483648)

    async def usertype(self, user_id: int) -> str:
        user = await self.col.find_one({"_id": user_id})
        return user.get("usertype", "Free")

    async def addpre(self, user_id: int) -> None:
        await self.col.update_one(
            {"_id": user_id},
            {"$set": {"usertype": "Premium", "uploadlimit": 4294967296}}  # 4GB
        )


# Initialize
agsbots = Database(Config.DB_URL, Config.DB_NAME)

# Example async startup call:
# await agsbots.init_indexes()
