from tanner import redis_client
import asyncio
import json
from tanner.sessions.session_analyzer import SessionAnalyzer
import time

async def tes():
	r= await redis_client.RedisClient.get_redis_client()
	print(r)
	await r.set("jojo","test is done")
	time.sleep(5)

	
async def ge(ids):
	print(ids)
	r= await redis_client.RedisClient.get_redis_client()
	print(r)
	y= await r.get(ids)
	session= json.loads(y)
	result = await SessionAnalyzer.create_stats(session, r)
	print(result)

def st(ids):
	print("getting the data as test")
	asyncio.run(tes())
	print("get func")
	asyncio.run(ge(ids))


