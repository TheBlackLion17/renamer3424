import motor.motor_asyncio
from config import Config
from .utils import send_log
agsbots = db["user"]

class Database:
    def total_user():
    user = agsbots.count_documents({})
    return user

# insert bot Data


def botdata(chat_id):
    bot_id = int(chat_id)
    try:
        bot_data = {"_id": bot_id, "total_rename": 0, "total_size": 0}
        agsbots.insert_one(bot_data)
    except:
        pass


def total_rename(chat_id, renamed_file):
    now = int(renamed_file) + 1
    agsbots.update_one({"_id": chat_id}, {"$set": {"total_rename": str(now)}})


def total_size(chat_id, total_size, now_file_size):
    now = int(total_size) + now_file_size
    agsbots.update_one({"_id": chat_id}, {"$set": {"total_size": str(now)}})


# insert user data
def insert(chat_id):
    user_id = int(chat_id)
    user_det = {"_id": user_id, "file_id": None, "caption": None, "daily": 0, "date": 0,
                "uploadlimit": 1288490188, "used_limit": 0, "usertype": "Free", "prexdate": None}
    try:
        agsbots.insert_one(user_det)
    except:
        return True
        pass


def addthumb(chat_id, file_id):
    agsbots.update_one({"_id": chat_id}, {"$set": {"file_id": file_id}})


def delthumb(chat_id):
    agsbots.update_one({"_id": chat_id}, {"$set": {"file_id": None}})


def addcaption(chat_id, caption):
    agsbots.update_one({"_id": chat_id}, {"$set": {"caption": caption}})


def delcaption(chat_id):
    agsbots.update_one({"_id": chat_id}, {"$set": {"caption": None}})


def dateupdate(chat_id, date):
    agsbots.update_one({"_id": chat_id}, {"$set": {"date": date}})


def used_limit(chat_id, used):
    agsbots.update_one({"_id": chat_id}, {"$set": {"used_limit": used}})


def usertype(chat_id, type):
    agsbots.update_one({"_id": chat_id}, {"$set": {"usertype": type}})


def uploadlimit(chat_id, limit):
    agsbots.update_one({"_id": chat_id}, {"$set": {"uploadlimit": limit}})


def addpre(chat_id):
    date = add_date()
    agsbots.update_one({"_id": chat_id}, {"$set": {"prexdate": date[0]}})


def addpredata(chat_id):
    agsbots.update_one({"_id": chat_id}, {"$set": {"prexdate": None}})


def daily(chat_id, date):
    agsbots.update_one({"_id": chat_id}, {"$set": {"daily": date}})


def find(chat_id):
    id = {"_id": chat_id}
    x = agsbots.find(id)
    for i in x:
        file = i["file_id"]
        try:
            caption = i["caption"]
        except:
            caption = None

        return [file, caption]


def getid():
    values = []
    for key in agsbots.find():
        id = key["_id"]
        values.append((id))
    return values

def delete(id):
    agsbots.delete_one(id)


def find_one(id):
    return agsbots.find_one({"_id": id})


    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.agsbots = self._client[database_name]
        self.col = self.agsbots.user

    def new_user(self, id):
        return dict(
            _id=int(id),                                   
            file_id=None,
            caption=None,
            prefix=None,
            suffix=None
        )

    async def add_user(self, b, m):
        u = m.from_user
        if not await self.is_user_exist(u.id):
            user = self.new_user(u.id)
            await self.col.insert_one(user)            
            await send_log(b, u)

    async def is_user_exist(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return bool(user)

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        all_users = self.col.find({})
        return all_users

    async def delete_user(self, user_id):
        await self.col.delete_many({'_id': int(user_id)})
    
    async def set_thumbnail(self, id, file_id):
        await self.col.update_one({'_id': int(id)}, {'$set': {'file_id': file_id}})

    async def get_thumbnail(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('file_id', None)

    async def set_caption(self, id, caption):
        await self.col.update_one({'_id': int(id)}, {'$set': {'caption': caption}})

    async def get_caption(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('caption', None)
        
    async def set_prefix(self, id, prefix):
        await self.col.update_one({'_id': int(id)}, {'$set': {'prefix': prefix}})  
        
    async def get_prefix(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('prefix', None)      
        
    async def set_suffix(self, id, suffix):
        await self.col.update_one({'_id': int(id)}, {'$set': {'suffix': suffix}})  
        
    async def get_suffix(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('suffix', None)              


agsbots = Database(Config.DB_URL, Config.DB_NAME)
