import asyncpg
# from constants import *
from privconstants import *


async def poolmanager():
    pool = await asyncpg.create_pool(user=dbuser, password=dbpass, database=db, host=dbadress)
    return pool
