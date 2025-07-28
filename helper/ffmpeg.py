import os
import time
import asyncio
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from typing import List


async def fix_thumb(thumb_path):
    """
    Fix the thumbnail image by resizing it and converting it to JPEG format.

    Args:
        thumb_path (str): Path to the thumbnail image.

    Returns:
        tuple: Width, height, and the path to the fixed thumbnail (or None if an error occurs).
    """
    width, height = 0, 0
    try:
        if thumb_path and os.path.exists(thumb_path):
            metadata = extractMetadata(createParser(thumb_path))
            if metadata:
                if metadata.has("width"):
                    width = metadata.get("width")
                if metadata.has("height"):
                    height = metadata.get("height")

            with Image.open(thumb_path) as img:
                img = img.convert("RGB")
                img = img.resize((320, height))  # Resize width to 320, keep original height
                img.save(thumb_path, "JPEG")

        return width, height, thumb_path
    except Exception as e:
        print(f"Error fixing thumbnail: {e}")
        return width, height, None


async def take_screen_shot(video_file, output_directory, ttl):
    """
    Take a screenshot from a video at a specific time.

    Args:
        video_file (str): Path to the video file.
        output_directory (str): Directory to save the screenshot.
        ttl (int): Time in seconds to take the screenshot.

    Returns:
        str: Path to the saved screenshot, or None if an error occurs.
    """
    try:
        out_put_file_name = os.path.join(output_directory, f"{int(time.time())}.jpg")

        cmd = [
            "ffmpeg",
            "-ss", str(ttl),
            "-i", video_file,
            "-vframes", "1",
            out_put_file_name,
        ]

        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        _, stderr = await process.communicate()

        if os.path.exists(out_put_file_name):
            return out_put_file_name
        else:
            print(f"FFmpeg error: {stderr.decode().strip()}")
            return None
    except Exception as e:
        print(f"Error in take_screen_shot: {e}")
        return None


def escape_invalid_curly_brackets(text: str, valids: List[str]) -> str:
    """
    Escape invalid curly brackets in the given text while preserving valid placeholders.

    Args:
        text (str): The input text containing curly brackets.
        valids (List[str]): A list of valid placeholder names (e.g., ["name", "age"]).

    Returns:
        str: The text with invalid curly brackets escaped.
    """
    new_text = []
    i = 0
    n = len(text)

    while i < n:
        if text[i] == "{":
            if i + 1 < n and text[i + 1] == "{":
                new_text.append("{{{{")
                i += 2
                continue

            valid_found = False
            for valid in valids:
                placeholder = "{" + valid + "}"
                if text.startswith(placeholder, i):
                    new_text.append(placeholder)
                    i += len(placeholder)
                    valid_found = True
                    break

            if not valid_found:
                new_text.append("{{")
                i += 1

        elif text[i] == "}":
            if i + 1 < n and text[i + 1] == "}":
                new_text.append("}}}}")
                i += 2
                continue

            new_text.append("}}")
            i += 1

        else:
            new_text.append(text[i])
            i += 1

    return "".join(new_text)
