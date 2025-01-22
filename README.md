
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

