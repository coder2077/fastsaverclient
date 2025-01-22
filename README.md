
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


## Examples

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

