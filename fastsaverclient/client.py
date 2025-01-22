import os
import httpx
import aiofiles
import shortuuid


class FastSaverClient:
	def __init__(self, token: str):
		self.token = token
		self.base_url = "https://fastsaverapi.com"
		self._client = httpx.AsyncClient(timeout=300, follow_redirects=True)

	async def get_info(self, url: str, db_cache: bool = False) -> dict:
		"""
		Fetch media details from the given URL.

		Args:
			url (str): The URL of the media to fetch info about (e.g., Instagram, TikTok, YouTube).
			db_cache (bool): If set to True, the method checks if the media has already been downloaded.
							If the media exists in the database, it returns the `channel_id` and `message_id`
							allowing the media to be directly sent (via `copyMessage`) in a Telegram bot.

		Returns:
			dict: A dictionary containing media details, such as:
				- `caption` (str): The caption of the media.
				- `thumb` (str): The thumbnail URL of the media.
				- `download_url` (str): The URL to download the media.
				- Other media-related data (e.g., duration, format, resolution).
				If `db_cache` is True, it may also include `channel_id` and `message_id` for easy message copying.

		Note:
			Each request to this method deducts 1 point from the user's balance.
		"""
		response = await self._client.get(
			url=f"{self.base_url}/get-info?url={url}&db_cache={db_cache}&token={self.token}"
		)
		return response.json()

	async def download_audio(self, shortcode: str) -> dict:
		"""
		Download audio from YouTube.

		Args:
			shortcode (str): The shortcode of the YouTube video from which to download the audio.

		Returns:
			dict: A dictionary containing `channel_id` and `message_id` if the audio is successfully 
				uploaded to Telegram. These values can be used with the `copyMessage` method in a 
				Telegram bot to send the audio message.

		Note:
			Each request to this method deducts 5 points from the user's balance.
		"""
		response = await self._client.get(
			url=f"{self.base_url}/download-audio?video_id={shortcode}&token={self.token}"
		)
		return response.json()

	async def get_top_musics(self, country: str, page: int) -> dict:
		"""
		Get top musics based on Shazam's rankings.

		Args:
			country (str): The country code (e.g., 'uz', 'ru', 'en') or 'world' to fetch global top musics.
			page (int): The page number to fetch (maximum 3 pages, with 10 results per page).

		Returns:
			dict: A dictionary containing the top musics, including details such as:
				- Music title
				- YouTube video shortcode

		Note:
			Each request to this method deducts 1 point from the user's balance.
			A maximum of 3 pages are available, with 10 results per page.
		"""
		response = await self._client.get(
			url=f"{self.base_url}/get-top-musics?country={country}&page={page}&token={self.token}"
		)
		return response.json()

	async def search_music(self, query: str, page: int = 1) -> dict:
		"""
		Search for music from YouTube.

		Args:
			query (str): The search query (e.g., song title, artist).
			page (int): The page number to fetch (default is 1). A maximum of 3 pages are available, 
						with 10 results per page.

		Returns:
			dict: A dictionary containing the search results, which include music title, shortcode, thumbnail and duration.

		Note:
			Each request to this method deducts 1 point from the user's balance.
			There are up to 3 pages available, with 10 results per page.
		"""
		response = await self._client.get(
			url=f"{self.base_url}/search-music?query={query}&page={page}&token={self.token}"
		)
		return response.json()

	async def recognize_music(self, file_url: str) -> dict:
		"""
		Recognize music from an audio or video file using Shazam.

		Args:
			file_url (str): The URL of the audio or video file to recognize. The file is processed through 
							Shazam to identify the music.

		Returns:
			dict: A dictionary containing the recognized music information, including details such as 
				the song title, artist, duation and other metadata based on Shazam's recognition. 
				If music is found, the top 5 YouTube results related to the music are also returned.

		Note:
			Each request to this method deducts 3 points from the user's balance.
		"""
		response = await self._client.get(
			url=f"{self.base_url}/recognize-music?file_url={file_url}&token={self.token}"
		)
		return response.json()

	async def get_music_lyrics(self, track_url: str) -> dict:
		"""
		Get lyrics for a music track using Shazam.

		Args:
			track_url (str): The URL of the music track, which is obtained after recognizing the music 
							using Shazam (e.g., from the `recognize_music` method).

		Returns:
			dict: A dictionary containing the lyrics for the music track.

		Note:
			Each request to this method deducts 3 points from the user's balance.
			This method relies on Shazam to retrieve the lyrics for the recognized track, so the 
			`track_url` must come from a valid recognition result.
		"""
		response = await self._client.get(
			url=f"{self.base_url}/get-music-lyrics?track_url={track_url}&token={self.token}"
		)
		return response.json()

	async def get_usage_stats(self, filter_by_token: bool = True) -> dict:
		"""
		Get usage statistics for the FastSaver API.

		Args:
			filter_by_token (bool): If set to True, the statistics will be filtered to show usage data 
									for the specific token provided. If set to False, the statistics 
									will include data for all tokens (i.e., all requests made by the user).

		Returns:
			dict: A dictionary containing usage statistics, such as the number of requests made, 
				the total data used, and other relevant metrics.

		Note:
			Each request to this method deducts 1 point from the user's balance.
		"""
		response = await self._client.get(
			url=f"{self.base_url}/get-usage-stats?filter_by_token={filter_by_token}&token={self.token}"
		)
		return response.json()

	async def save_video(self, url: str, file_name: str = None) -> str | None:
		"""
		Save a video from a given URL.

		Args:
			url (str): The URL of the video to be saved.
			file_name (str): The name of the file to be saved. If not provided, a random name will be generated.

		Returns:
			str: The name of the saved file, or None if the file could not be saved.
		"""
		if file_name is None:
			file_name = f"downloads/{shortuuid.uuid()}.mp4"
			os.makedirs(os.path.dirname(file_name), exist_ok=True)
		try:
			response = await self._client.get(url)
			response.raise_for_status()
			async with aiofiles.open(file_name, 'wb') as f:
				await f.write(response.content)
			return file_name
		except Exception as e:
			print(e)
			return None

	async def add_cached_media(self, secret: str, shortcode: str, channel_id: int, message_id: int, media_type: str) -> dict:
		"""
		Add cached media to the FastSaver API Database.

		Args:
			secret (str): The secret key.
			shortcode (str): The shortcode of the media.
			channel_id (int): The ID of the channel.
			message_id (int): The ID of the message.
			media_type (str): The type of the media.

		Returns:
			dict: A dictionary containing the response.

		Note:
			This endpoint is not publicly accessible.
		"""
		response = await self._client.get(
			url=f"{self.base_url}/add-cached-media?secret={secret}&shortcode={shortcode}&channel_id={channel_id}&message_id={message_id}&media_type={media_type}"
		)
		return response.json()

	async def close(self) -> None:
		"""Close the underlying HTTP client."""
		await self._client.aclose()

