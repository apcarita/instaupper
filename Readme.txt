# InstaUpper

InstaUpper is a Python script that automates the process of uploading video reels to Instagram. It uses a headless browser to interact with Instagram's web interface, allowing you to post videos without manual intervention.

## Features

- Automatically logs into Instagram using saved cookies or credentials.
- Uploads video files from a specified directory.
- Sets the video title based on the file name.

## Requirements

- Python 3.7+
- `asyncio`
- `dotenv`
- `nodriver` (or any other headless browser driver)
- `pathlib`

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/instaupper.git
    cd instaupper
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your Instagram credentials:
    ```env
    EMAIL_USERNAME=your_instagram_email
    EMAIL_PASSWORD=your_instagram_password
    ```

4. Place the video files you want to upload in the `To_Upload` directory.

## Usage

Run the `RunPosts.py` script to start uploading videos:
```sh
python RunPosts.py
```

The script will loop through each video file in the `To_Upload` directory and post it to Instagram using the `postReel` function.

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.
