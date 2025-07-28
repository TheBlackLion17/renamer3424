import math
import time
from datetime import datetime
from typing import Optional
from pytz import timezone
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User
from config import Config, Txt


async def progress_for_pyrogram(
    current: int,
    total: int,
    ud_type: str,
    message: Message,
    start: float,
    update_interval: int = 5,
):
    """
    Update progress bar in a Telegram message during upload/download.

    Args:
        current (int): Current progress in bytes.
        total (int): Total file size in bytes.
        ud_type (str): Action type (Uploading/Downloading).
        message (Message): Telegram message object to edit.
        start (float): Start time (from time.time()).
        update_interval (int): Seconds between updates.
    """
    now = time.time()
    diff = now - start

    if round(diff % update_interval) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff if diff > 0 else 0
        elapsed_time = round(diff * 1000)
        time_remaining = round((total - current) / speed * 1000) if speed > 0 else 0
        total_time = elapsed_time + time_remaining

        estimated_total_time_str = TimeFormatter(total_time)

        progress_bar = "{0}{1}".format(
            "█" * math.floor(percentage / 5),
            "░" * (20 - math.floor(percentage / 5)),
        )

        progress_message = Txt.PROGRESS_BAR.format(
            round(percentage, 2),
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            estimated_total_time_str or "0s"
        )

        try:
            await message.edit(
                text=f"{ud_type}\n\n{progress_bar}\n{progress_message}",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("✖️ 𝖢𝖺𝗇𝖼𝖾𝗅 ✖️", callback_data="close")]]
                ),
            )
        except Exception as e:
            print(f"[Progress Edit Error] {e}")


def humanbytes(size: float) -> str:
    """
    Convert bytes to a human-readable format.

    Args:
        size (float): File size in bytes.

    Returns:
        str: Readable file size (e.g., "1.2 MB").
    """
    if not size:
        return "0 B"

    power = 2**10
    labels = {0: "B", 1: "KB", 2: "MB", 3: "GB", 4: "TB"}
    n = 0

    while size >= power and n < len(labels) - 1:
        size /= power
        n += 1

    return f"{round(size, 2)} {labels[n]}"


def TimeFormatter(milliseconds: int) -> str:
    """
    Convert milliseconds to a human-readable time format.

    Args:
        milliseconds (int): Duration in milliseconds.

    Returns:
        str: Time like "1d, 2h, 3m, 4s".
    """
    seconds, ms = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    parts = []
    if days: parts.append(f"{days}d")
    if hours: parts.append(f"{hours}h")
    if minutes: parts.append(f"{minutes}m")
    if seconds: parts.append(f"{seconds}s")
    if ms: parts.append(f"{ms}ms")

    return ", ".join(parts) if parts else "0s"


def convert(seconds: int) -> str:
    """
    Convert seconds to HH:MM:SS format.

    Args:
        seconds (int): Duration in seconds.

    Returns:
        str: Formatted string.
    """
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{hour:02d}:{minutes:02d}:{seconds:02d}"


async def send_log(bot, user: User):
    """
    Send a user log message to LOG_CHANNEL.

    Args:
        bot: Pyrogram Client instance.
        user (User): The user who started the bot.
    """
    if Config.LOG_CHANNEL:
        curr = datetime.now(timezone("Asia/Kolkata"))
        date = curr.strftime("%d %B, %Y")
        time_str = curr.strftime("%I:%M:%S %p")

        log_message = (
            f"<b><u>📥 New User Started Bot</u></b>\n\n"
            f"<b>👤 Name</b>: {user.mention}\n"
            f"<b>🆔 User ID</b>: <code>{user.id}</code>\n"
            f"<b>🔤 First Name</b>: {user.first_name}\n"
            f"<b>🔡 Last Name</b>: {user.last_name or 'N/A'}\n"
            f"<b>💬 Username</b>: @{user.username or 'N/A'}\n"
            f"<b>🔗 Profile</b>: <a href='tg://user?id={user.id}'>Click Here</a>\n\n"
            f"<b>📅 Date</b>: {date}\n"
            f"<b>🕒 Time</b>: {time_str}"
        )

        try:
            await bot.send_message(Config.LOG_CHANNEL, log_message)
        except Exception as e:
            print(f"[Log Send Error] {e}")
