# FastSaverClient

A Python client for interacting with the FastSaver API to download and manage media content.

## Installation

Install via pip:

```bash
pip install fastsaverclient
Usage
Initialize Client
python
Copy
Edit
from fastsaverclient import FastSaverClient

client = FastSaverClient(token="YOUR_API_TOKEN")
Available Methods
get_info(url: str, db_cache: bool = False)
Fetches media details.

python
Copy
Edit
info = await client.get_info(url="MEDIA_URL")
Arguments:

url (str): The URL of the media to fetch info about (e.g., Instagram, TikTok, YouTube).
db_cache (bool): If True, checks the media in the database. If found, returns channel_id and message_id.
Returns:

A dictionary containing media details like caption, thumbnail, download URL, and more.
download_audio(shortcode: str)
Downloads audio from YouTube.

python
Copy
Edit
audio = await client.download_audio(shortcode="YOUTUBE_SHORTCODE")
Arguments:

shortcode (str): The shortcode of the YouTube video to download audio from.
Returns:

A dictionary containing channel_id and message_id if the audio is successfully uploaded to Telegram.
get_top_musics(country: str, page: int)
Fetches top musics based on Shazam rankings.

python
Copy
Edit
top_musics = await client.get_top_musics(country="uz", page=1)
Arguments:

country (str): The country code ('uz', 'ru', etc.) or 'world' for global music.
page (int): The page number to fetch (1–3, 10 results per page).
Returns:

A dictionary containing top music details such as title, YouTube shortcode, etc.
search_music(query: str, page: int = 1)
Searches for music on YouTube.

python
Copy
Edit
search = await client.search_music(query="Song Title")
Arguments:

query (str): The search query (e.g., song title, artist).
page (int): The page number to fetch (default is 1).
Returns:

A dictionary containing search results, including music title, shortcode, thumbnail, and duration.
recognize_music(file_url: str)
Recognizes music from audio or video file.

python
Copy
Edit
recognition = await client.recognize_music(file_url="FILE_URL")
Arguments:

file_url (str): The URL of the audio or video file to recognize.
Returns:

A dictionary containing recognized music information (song title, artist, duration, etc.) and top YouTube results.
get_music_lyrics(track_url: str)
Fetches lyrics for a recognized music track.

python
Copy
Edit
lyrics = await client.get_music_lyrics(track_url="TRACK_URL")
Arguments:

track_url (str): The URL of the music track obtained from the recognize_music method.
Returns:

A dictionary containing the lyrics of the track.
get_usage_stats(filter_by_token: bool = True)
Fetches usage statistics.

python
Copy
Edit
stats = await client.get_usage_stats()
Arguments:

filter_by_token (bool): If True, shows stats for the current token. If False, shows stats for all tokens.
Returns:

A dictionary containing usage statistics, such as the number of requests made and total data used.
save_video(url: str, file_name: Optional[str] = None)
Saves a video from a given URL.

python
Copy
Edit
saved_video = await client.save_video(url="VIDEO_URL")
Arguments:

url (str): The URL of the video to be saved.
file_name (Optional[str]): The name of the file to save. If None, a random name is generated.
Returns:

The saved file name if successful, or None if the video could not be saved.
add_cached_media(secret: str, shortcode: str, channel_id: int, message_id: int, media_type: str)
Adds cached media (private endpoint).

python
Copy
Edit
cache = await client.add_cached_media(secret="SECRET", shortcode="SHORTCODE", channel_id=123, message_id=456, media_type="audio")
Arguments:

secret (str): The secret key.
shortcode (str): The shortcode of the media.
channel_id (int): The ID of the channel.
message_id (int): The ID of the message.
media_type (str): The type of the media (e.g., audio, video).
Returns:

A dictionary containing the response from the API.
Closing the Client
python
Copy
Edit
await client.close()
This closes the underlying HTTP client.

Notes
Each request deducts points from your balance.
Ensure proper error handling for production environments.
Use get_usage_stats() to monitor your balance and usage.
