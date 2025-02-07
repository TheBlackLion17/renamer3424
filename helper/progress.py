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
        elapsed_time_str = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time_str = TimeFormatter(milliseconds=estimated_total_time)

        # Create progress bar
        progress_bar = "[{0}{1}]".format(
            "●" * math.floor(percentage / 5),
            "○" * (20 - math.floor(percentage / 5)),
        )

        # Create progress message
        progress_message = (
            f"{progress_bar}\n"
            f"**Progress**: {round(percentage, 2)}%\n"
            f"{humanbytes(current)} of {humanbytes(total)}\n"
            f"**Speed**: {humanbytes(speed)}/s\n"
            f"**ETA**: {estimated_total_time_str if estimated_total_time_str else '0 s'}"
        )

        # Update the Telegram message
        try:
            await message.edit(text=f"{ud_type}\n{progress_message}")
        except Exception as e:
            print(f"Failed to update progress message: {e}")


def humanbytes(size: float) -> str:
    """
    Convert a file size in bytes to a human-readable format.

    Args:
        size (float): File size in bytes.

    Returns:
        str: Human-readable file size (e.g., "1.23 MiB").
    """
    if not size:
        return "0 B"

    power = 2**10
    n = 0
    size_labels = {0: "B", 1: "KiB", 2: "MiB", 3: "GiB", 4: "TiB"}

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
