import ast
import asyncio
import poolmanager


class database:
    def __init__(self, chatid):
        self.loop = asyncio.get_event_loop()
        self.chatid = chatid

    async def getusers(self):
        pool1 = await poolmanager.poolmanager()
        async with pool1.acquire() as conn:
            users = await conn.fetch('SELECT userid FROM users WHERE chatid = $1', int(self.chatid))
            users = str(users).replace(">", "").replace("<Record userid=", "")
            users = ast.literal_eval(users)
        return users

    async def getusername(self, userid):
        pool1 = await poolmanager.poolmanager()
        async with pool1.acquire() as conn:
            r = await conn.fetchval('SELECT firstname FROM users WHERE chatid = $1 AND userid = $2', int(self.chatid),
                                    int(userid))
            print(r)
            return r
