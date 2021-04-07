from aiogram.utils import json
from aiohttp import web

import modules


async def ttl(request):
    req = await request.json()
    print(req)
    chatid = req["chatid"]
    return web.json_response(await modules.userofday(chatid))


async def reset(request):
    print("reset")


async def stats(request):
    print('stats')


async def init(request):
    print("init")


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.post('/ttl', ttl)])
    app.add_routes([web.post('/rst', reset)])
    app.add_routes([web.post('/stats', stats)])
    app.add_routes([web.post('/init', init)])
    web.run_app(app, host="0.0.0.0", port=1111)
