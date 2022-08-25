from tanner import redis_client as r
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
	redis_client= await r.RedisClient.get_redis_client()
	print(r)
	y= await redis_client.get(ids)
	session= json.loads(y)
	print(session)
	result = await SessionAnalyzer.create_stats(session, redis_client)
	print(result)

def st(ids):
	#print("getting the data as test")
	#asyncio.run(tes())
	print("get func")
	asyncio.run(ge(ids))


