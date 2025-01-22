
# FastSaverClient

A Python client for interacting with the FastSaver API to download and manage media content.




## Installation

Install via pip:

```
pip install fastsaverclient
```
## Usage/Examples

```python
from fastsaverclient import FastSaverClient

client = FastSaverClient(token="yGo77fiHlgDOE9L0qHPcJHHF")

async def main():
  resp = await client.get_info("https://www.instagram.com/reel/Bzn_mYKAltF/")
  print(resp)

if __name__ == "__main__":
  import asyncio
  asyncio.run(main())
```

Available Methods
1. get_info(url: str, db_cache: bool = False)
Fetches media details, including captions, thumbnails, and download URLs.

2. download_audio(shortcode: str)
Downloads audio from YouTube using the video shortcode.

3. get_top_musics(country: str, page: int)
Fetches the top Shazam music rankings for a specific country or globally.

4. search_music(query: str, page: int = 1)
Searches YouTube for music based on a query.

5. recognize_music(file_url: str)
Recognizes a song from an audio or video file URL.

6. get_music_lyrics(track_url: str)
Fetches lyrics for a recognized track.

7. get_usage_stats(filter_by_token: bool = True)
Fetches API usage statistics for your account.

8. save_video(url: str, file_name: Optional[str] = None)
Downloads and saves a video locally.

9. add_cached_media(secret: str, shortcode: str, channel_id: int, message_id: int, media_type: str)
Adds a media item to the API's cache (private method).

10. close()
Closes the underlying HTTP client.

