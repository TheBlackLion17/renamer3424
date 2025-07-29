import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime, date as date_
from helper.progress import humanbytes
from helper.database import agsbots  # <- use the object with methods
from helper.date import check_expi

@Client.on_message(filters.private & filters.command(["myplan"]))
async def start(client, message):
    user_id = message.from_user.id
    used_ = await agsbots.col.find_one({"_id": user_id})

    if not used_:
        await message.reply("⚠️ You are not in the database. Please use /start.")
        return

    # 🗓 Daily reset logic
    today_str = date_.today().isoformat()
    if used_.get("daily") != today_str:
        await agsbots.col.update_one({"_id": user_id}, {
            "$set": {"daily": today_str, "used_limit": 0}
        })

    # Fetch updated user data
    user_data = await agsbots.col.find_one({"_id": user_id})
    used = user_data.get("used_limit", 0)
    limit = user_data.get("uploadlimit", 2147483648)
    remain = limit - used
    user = user_data.get("usertype", "Free")
    ends = user_data.get("prexdate")

    # 🔄 Check for expired premium
    if ends:
        if not check_expi(ends):
            await agsbots.col.update_one({"_id": user_id}, {
                "$set": {"uploadlimit": 1288490188, "usertype": "Free"}
            })
            user = "Free"
            limit = 1288490188
            remain = limit - used

    # 📄 Prepare text
    text = f"User ID:- ```{user_id}```\nPlan :- {user}\nDaily Upload Limit :- {humanbytes(limit)}\nToday Used :- {humanbytes(used)}\nRemain:- {humanbytes(remain)}"

    if ends:
        normal_date = datetime.fromtimestamp(ends).strftime('%Y-%m-%d')
        text += f"\n\nYour Plan Ends On :- {normal_date}"

    # 💬 Reply
    if user == "Free":
        await message.reply(
            text,
            quote=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Upgrade 💰💳", callback_data="upgrade"),
                InlineKeyboardButton("Cancel ✖️", callback_data="cancel")
            ]])
        )
    else:
        await message.reply(text, quote=True)
