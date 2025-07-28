import math
import time
from typing import Optional


async def progress_for_pyrogram(
    current: int,
    total: int,
    ud_type: str,
    message,
    start: float,
    update_interval: int = 10,
):
    """
    Track and update the progress of an operation in a Telegram message.

    Args:
        current (int): Current progress value.
        total (int): Total progress value.
        ud_type (str): Type of operation (e.g., "Uploading", "Downloading").
        message: The Telegram message object to edit.
        start (float): Start time in seconds since epoch.
        update_interval (int): Time interval (in seconds) to update the message.
    """
    now = time.time()
    diff = now - start

    # Update only every `update_interval` seconds or at the end
    if current == total or int(diff) % update_interval == 0:
        try:
            percentage = current * 100 / total
            speed = current / diff if diff > 0 else 0
            elapsed_time = round(diff * 1000)
            time_left = round((total - current) / speed * 1000) if speed > 0 else 0
            estimated_time = elapsed_time + time_left

            elapsed_str = TimeFormatter(milliseconds=elapsed_time)
            total_str = TimeFormatter(milliseconds=estimated_time)

            progress_bar = "[{0}{1}]".format(
                "●" * math.floor(percentage / 5),
                "○" * (20 - math.floor(percentage / 5)),
            )

            progress_message = (
                f"{progress_bar}\n"
                f"**Progress**: `{round(percentage, 2)}%`\n"
                f"`{humanbytes(current)} of {humanbytes(total)}`\n"
                f"**Speed**: `{humanbytes(speed)}/s`\n"
                f"**ETA**: `{total_str}`"
            )

            await message.edit(text=f"**{ud_type}**\n{progress_message}")
        except Exception as e:
            print(f"[Progress Update Error]: {e}")


def humanbytes(size: float) -> str:
    """
    Convert bytes into a human-readable format.

    Args:
        size (float): Size in bytes.

    Returns:
        str: Human-readable string (e.g., "1.2 MiB").
    """
    if not size:
        return "0 B"

    power = 2 ** 10
    n = 0
    units = ["B", "KiB", "MiB", "GiB", "TiB"]

    while size >= power and n < len(units) - 1:
        size /= power
        n += 1

    return f"{round(size, 2)} {units[n]}"


def TimeFormatter(milliseconds: int) -> str:
    """
    Convert milliseconds into a readable duration string.

    Args:
        milliseconds (int): Time in milliseconds.

    Returns:
        str: Formatted string like "1d, 2h, 3m, 4s"
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
