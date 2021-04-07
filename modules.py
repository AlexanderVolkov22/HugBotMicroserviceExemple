from classes import randomorgmodule
from classes.database import database
from privconstants import randomorg


async def random(chatid):
    users = database
    users = await users(chatid).getusers()
    count = len(users)
    c = await randomorgmodule.random(randomorg, 0, count - 1, 1).rand()
    resp = users[c]
    print(resp)
    return resp


async def userofday(chatid):
    db = database
    userid = await random(chatid)
    username = await db(chatid).getusername(userid)
    js = {'Status': 'Ok', 'userid': userid, 'username': username}
    return js
