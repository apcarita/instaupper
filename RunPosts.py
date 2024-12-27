import asyncio
from pathlib import Path
from Main import postReel
from Xupper import postX
import nodriver as uc
import os
from datetime import datetime

async def main():
    to_upload_dir = Path("To_Upload")
    uploaded_dir = Path("Uploaded")
    uploaded_dir.mkdir(exist_ok=True)
    video_files = to_upload_dir.glob("*.mp4")

    for video_file in video_files:
        title = video_file.stem  # Use the file name (without extension) as the title
        success = await postX(str(video_file), title)
        if success:
            video_file.rename(uploaded_dir / video_file.name)

def log(title, platform):
    log_dir = "log"

    with open(log_dir, "a") as log_file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Script ran at: {current_time} | Uploaded file: {title}\n to {platform}")
        log_file.write(f"Script ran at: {current_time} | Uploaded file: {title}\n")

if __name__ == "__main__":
    to_upload_dir = Path("To_Upload")
    uploaded_dir = Path("Uploaded")
    uploaded_dir.mkdir(exist_ok=True)
    video_files = to_upload_dir.glob("*.mp4")

    hashtags = ['#faith', '#religion', '#spirituality', '#bible', '#god', '#jesus', '#christianity']

    for video_file in video_files:
        title = video_file.stem + " " + " ".join(hashtags)  # Use the file name (without extension) as the title
        file_dir = str(video_file)
        try:
            print("uploading to X")
            #uc.loop().run_until_complete(postX(file_dir, title))
            #log(title, "X")
        except:
            print("Failed to upload to X")
        try:
            print("uploading to Instagram")
            uc.loop().run_until_complete(postReel(file_dir, title))
            log(title, "Instagram")
        except:
            print("Failed to upload to Instagram")

        video_file.rename(uploaded_dir / video_file.name)


        