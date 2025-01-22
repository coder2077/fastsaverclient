FastSaverClient
The FastSaverClient is a Python library designed to interact with the FastSaver API, allowing you to download, fetch details, recognize, and search for media content, including music and videos. This client uses asynchronous requests and is ideal for building applications or bots that require media-related features, such as video downloads, music recognition, and lyrics fetching.

Installation
You can install the FastSaverClient using pip:

bash
Copy
Edit
pip install fastsaverclient
Usage
Initializing the Client
To use the FastSaverClient, first initialize it with your FastSaver API token:

python
Copy
Edit
from fastsaverclient import FastSaverClient

token = "YOUR_API_TOKEN"
client = FastSaverClient(token)
Methods
Here are the available methods you can use:

get_info
Fetches media details from the given URL.

python
Copy
Edit
info = await client.get_info(url="URL_OF_MEDIA", db_cache=False)
Args:
url (str): The URL of the media (e.g., Instagram, TikTok, YouTube).
db_cache (bool): If True, checks if the media is already cached in the database.
Returns:
A dictionary with media details, such as caption, thumbnail URL, download URL, and more.
Points Deducted: 1 point per request.
download_audio
Downloads audio from a YouTube video.

python
Copy
Edit
audio_info = await client.download_audio(shortcode="YOUTUBE_SHORTCODE")
Args:

shortcode (str): The YouTube video's shortcode.
Returns:

A dictionary containing channel_id and message_id, which can be used for sending the audio in Telegram.
Points Deducted: 5 points per request.

get_top_musics
Fetches top music tracks based on Shazam's rankings.

python
Copy
Edit
top_musics = await client.get_top_musics(country="uz", page=1)
Args:

country (str): Country code (e.g., uz, ru, en) or world for global top music.
page (int): The page number (max 3 pages, 10 results per page).
Returns:

A dictionary containing the top music titles and YouTube video shortcodes.
Points Deducted: 1 point per request.

search_music
Searches for music from YouTube.

python
Copy
Edit
search_results = await client.search_music(query="Song Title")
Args:

query (str): The search query (e.g., song title, artist).
page (int): The page number (max 3 pages, 10 results per page).
Returns:

A dictionary containing music title, shortcode, thumbnail, and duration.
Points Deducted: 1 point per request.

recognize_music
Recognizes music from an audio or video file.

python
Copy
Edit
recognition_results = await client.recognize_music(file_url="FILE_URL")
Args:

file_url (str): The URL of the audio or video file to recognize.
Returns:

A dictionary containing recognized music details, including song title, artist, and YouTube results.
Points Deducted: 3 points per request.

get_music_lyrics
Fetches lyrics for a recognized music track.

python
Copy
Edit
lyrics = await client.get_music_lyrics(track_url="TRACK_URL")
Args:

track_url (str): The URL of the recognized music track (from the recognize_music method).
Returns:

A dictionary containing the lyrics of the music.
Points Deducted: 3 points per request.

get_usage_stats
Fetches usage statistics for the FastSaver API.

python
Copy
Edit
stats = await client.get_usage_stats(filter_by_token=True)
Args:

filter_by_token (bool): If True, stats are filtered by the provided token.
Returns:

A dictionary containing usage data such as number of requests made and total data used.
Points Deducted: 1 point per request.

save_video
Saves a video from a given URL.

python
Copy
Edit
saved_video = await client.save_video(url="VIDEO_URL")
Args:

url (str): The URL of the video.
file_name (str): Optional name for the saved file. If not provided, a random name is generated.
Returns:

The name of the saved file or None if the video couldn't be saved.
add_cached_media
Adds cached media to the FastSaver API Database (private endpoint).

python
Copy
Edit
cache_response = await client.add_cached_media(secret="SECRET", shortcode="SHORTCODE", channel_id=123, message_id=456, media_type="audio")
Args:

secret (str): The secret key for adding cached media.
shortcode (str): The shortcode of the media.
channel_id (int): The ID of the channel.
message_id (int): The ID of the message.
media_type (str): The type of the media (e.g., "audio", "video").
Returns:

A dictionary containing the response.
Closing the Client
Don't forget to close the client after use:

python
Copy
Edit
await client.close()
Notes
Each request to these methods deducts points from the user's balance.
The methods rely on the FastSaver API for fetching media, downloading content, and recognizing music.
Ensure to handle exceptions and errors when making requests.
That's it! With this client, you can easily interact with the FastSaver API and build media-related functionality into your projects.
