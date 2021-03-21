from aiohttp import web


async def pdr(request):
    print("pdr")


async def ttl(request):
    print("ttl")


async def reset(request):
    print("reset")


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.post('/pdr', pdr)])
    app.add_routes([web.post('/ttl', ttl)])
    app.add_routes([web.post('/rst', reset)])
    web.run_app(app, host="0.0.0.0", port=1111)
