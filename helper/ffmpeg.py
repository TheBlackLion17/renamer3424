import time
import os
import asyncio
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser


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
            # Extract metadata to get width and height
            metadata = extractMetadata(createParser(thumb_path))
            if metadata and metadata.has("width"):
                width = metadata.get("width")
            if metadata and metadata.has("height"):
                height = metadata.get("height")

            # Open, convert, and resize the image
            with Image.open(thumb_path) as img:
                img = img.convert("RGB")
                img = img.resize((320, height))  # Resize to a width of 320 while maintaining aspect ratio
                img.save(thumb_path, "JPEG")  # Save as JPEG

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
        # Generate a unique output file name
        out_put_file_name = os.path.join(output_directory, f"{int(time.time())}.jpg")

        # FFmpeg command to extract a screenshot
        file_genertor_command = [
            "ffmpeg",
            "-ss", str(ttl),  # Seek to the specified time
            "-i", video_file,  # Input video file
            "-vframes", "1",  # Extract only one frame
            out_put_file_name,  # Output file
        ]

        # Run the FFmpeg command asynchronously
        process = await asyncio.create_subprocess_exec(
            *file_genertor_command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()

        # Check if the screenshot was successfully created
        if os.path.exists(out_put_file_name):
            return out_put_file_name
        else:
            print(f"Error generating screenshot: {stderr.decode().strip()}")
            return None
    except Exception as e:
        print(f"Error in take_screen_shot: {e}")
        return None
