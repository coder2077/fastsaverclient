
# FastSaverClient

A Python async client for interacting with the FastSaver API.


## Installation

Install via pip:

```bash
pip install fastsaverclient
```
### Available Methods

- **`get_info(url: str, db_cache: bool = False)`**  
  Fetch media details from the given URL.

- **`download_audio(shortcode: str)`**  
  Download audio from YouTube.

- **`get_top_musics(country: str, page: int)`**  
  Get top musics based on Shazam's rankings.

- **`search_music(query: str, page: int = 1)`**  
  Search for music from YouTube.

- **`recognize_music(file_url: str)`**  
  Recognize music from an audio or video file using Shazam.

- **`get_music_lyrics(track_url: str)`**  
  Get lyrics for a music track using Shazam.

- **`get_usage_stats(filter_by_token: bool = True)`**  
  Get usage statistics for the FastSaver API.

- **`save_video(url: str, file_name: Optional[str] = None)`**  
  Save a video from a given URL.


## Usage

```python
from fastsaverclient import FastSaverClient

client = FastSaverClient(token="API_TOKEN_HERE")

async def main():
  resp = await client.get_info("https://www.instagram.com/reel/Bzn_mYKAltF/")
  print(resp['download_url'])

if __name__ == "__main__":
  import asyncio
  asyncio.run(main())
```

Downloading Youtube video and sending it user with aiogram
```python
from aiogram import Bot
from fastsaverclient import FastSaverClient

# Initialize the Bot and FastSaverClient with tokens
bot = Bot(token="YOUR_BOT_TOKEN")
client = FastSaverClient(token="YOUR_API_TOKEN")

async def main():
	# Fetch media info from the URL
	info = await client.get_info("https://www.youtube.com/watch?v=-qUPSRx9Rfk")
	print(f"Video Info: {info}")

	# Extract the 720p download URL
	url_720p = next((item['download_url'] for item in info['formats'] if item['format'] == '720p'), None)

	print(f"720p Download URL: {url_720p}")

	# Download the file (audio/video) from the URL
	downloaded_file = await client._client.get(url_720p)
	downloaded_file = downloaded_file.json()

	# Send the downloaded file to the user
	await bot.copy_message(
		chat_id=1,  # Target chat ID (can be user ID or group ID)
		from_chat_id=downloaded_file['channel_id'],
		message_id=downloaded_file['message_id'],
		caption=info['title']  # Caption with the video title
	)

if __name__ == "__main__":
	import asyncio
	asyncio.run(main())
```
