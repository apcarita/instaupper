import asyncio
from pathlib import Path
from Main import postReel

async def main():
    to_upload_dir = Path("To_Upload")
    video_files = to_upload_dir.glob("*.mp4")

    for video_file in video_files:
        title = video_file.stem  # Use the file name (without extension) as the title
        await postReel(str(video_file), title)

if __name__ == "__main__":
    asyncio.run(main())
