import math
import time
from datetime import datetime
from typing import Optional
from pytz import timezone
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import Config, Txt


async def progress_for_pyrogram(
    current: int,
    total: int,
    ud_type: str,
    message,
    start: float,
    update_interval: int = 5,
):
    """
    Track and update the progress of an operation in a Telegram message.

    Args:
        current (int): Current progress value.
        total (int): Total progress value.
        ud_type (str): Type of operation (e.g., "Uploading", "Downloading").
        message: The Telegram message object to edit.
        start (float): Start time of the operation (in seconds since epoch).
        update_interval (int): Interval in seconds to update the progress message.
    """
    now = time.time()
    diff = now - start

    # Update progress only if the interval has passed or the operation is complete
    if round(diff % update_interval) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff if diff > 0 else 0
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000 if speed > 0 else 0
        estimated_total_time = elapsed_time + time_to_completion

        # Format elapsed and estimated time
        estimated_total_time_str = TimeFormatter(milliseconds=estimated_total_time)

        # Create progress bar
        progress_bar = "{0}{1}".format(
            "█" * math.floor(percentage / 5),
            "░" * (20 - math.floor(percentage / 5)),
        )

        # Create progress message
        progress_message = Txt.PROGRESS_BAR.format(
            round(percentage, 2),
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            estimated_total_time_str if estimated_total_time_str else "0 s",
        )

        # Update the Telegram message
        try:
            await message.edit(
                text=f"{ud_type}\n\n{progress_bar}\n{progress_message}",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("✖️ 𝖢𝖺𝗇𝖼𝖾𝗅 ✖️", callback_data="close")]]
                ),
            )
        except Exception as e:
            print(f"Failed to update progress message: {e}")


def humanbytes(size: float) -> str:
    """
    Convert a file size in bytes to a human-readable format.

    Args:
        size (float): File size in bytes.

    Returns:
        str: Human-readable file size (e.g., "1.23 MB").
    """
    if not size:
        return "0 B"

    power = 2**10
    size_labels = {0: "B", 1: "KB", 2: "MB", 3: "GB", 4: "TB"}
    n = 0

    while size >= power and n < len(size_labels) - 1:
        size /= power
        n += 1

    return f"{round(size, 2)} {size_labels[n]}"


def TimeFormatter(milliseconds: int) -> str:
    """
    Convert milliseconds to a human-readable time format.

    Args:
        milliseconds (int): Time duration in milliseconds.

    Returns:
        str: Human-readable time format (e.g., "1d, 2h, 3m, 4s").
    """
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    time_parts = []
    if days:
        time_parts.append(f"{days}d")
    if hours:
        time_parts.append(f"{hours}h")
    if minutes:
        time_parts.append(f"{minutes}m")
    if seconds:
        time_parts.append(f"{seconds}s")
    if milliseconds:
        time_parts.append(f"{milliseconds}ms")

    return ", ".join(time_parts) if time_parts else "0s"


def convert(seconds: int) -> str:
    """
    Convert seconds to a formatted time string (HH:MM:SS).

    Args:
        seconds (int): Time duration in seconds.

    Returns:
        str: Formatted time string (e.g., "01:23:45").
    """
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{hour:02d}:{minutes:02d}:{seconds:02d}"


async def send_log(bot, user):
    """
    Send a log message to the configured log channel when a new user starts the bot.

    Args:
        bot: The bot instance.
        user: The user who started the bot.
    """
    if Config.LOG_CHANNEL:
        curr = datetime.now(timezone("Asia/Kolkata"))
        date = curr.strftime("%d %B, %Y")
        time = curr.strftime("%I:%M:%S %p")

        log_message = (
            f"<b><u>𝖭𝖾𝗐 𝖴𝗌𝖾𝗋 𝖲𝗍𝖺𝗋𝗍𝖾𝖽 𝖳𝗁𝖾 𝖡𝗈𝗍</u></b>\n\n"
            f"<b>𝖴𝗌𝖾𝗋 𝖬𝖾𝗇𝗍𝗂𝗈𝗇</b> : {user.mention}\n"
            f"<b>𝖴𝗌𝖾𝗋 𝖨𝖣</b> : `{user.id}`\n"
            f"<b>𝖥𝗂𝗋𝗌𝗍 𝖭𝖺𝗆𝖾</b> : {user.first_name}\n"
            f"<b>𝖫𝖺𝗌𝗍 𝖭𝖺𝗆𝖾</b> : {user.last_name}\n"
            f"<b>𝖴𝗌𝖾𝗋 𝖭𝖺𝗆𝖾</b> : @{user.username}\n"
            f"<b>𝖴𝗌𝖾𝗋 𝖫𝗂𝗇𝗄</b> : <a href='tg://openmessage?user_id={user.id}'>𝖢𝗅𝗂𝖼𝗄 𝖧𝖾𝗋𝖾</a>\n\n"
            f"<b>𝖣𝖺𝗍𝖾</b> : {date}\n"
            f"<b>𝖳𝗂𝗆𝖾</b> : {time}"
        )

        await bot.send_message(Config.LOG_CHANNEL, log_message)
