import asyncio
import aiohttp


class random:
    def __init__(self, apikey, min, max, n):
        self.loop = asyncio.get_event_loop()
        self.apikey = apikey
        self.min = min
        self.max = max
        self.n = n

    async def rand(self):
        js = {
            "jsonrpc": "2.0",
            "method": "generateIntegers",
            "params": {
                "apiKey": self.apikey,
                "n": self.n,
                "min": self.min,
                "max": self.max
            },
            "id": 1
        }
        async with aiohttp.ClientSession() as session:
            async with session.post("https://api.random.org/json-rpc/2/invoke", json=js) as resp:
                resp = await resp.json(content_type='application/json')
                resp = resp['result']['random']['data'][0]
                return resp

