from tanner import redis_client
import asyncio
import json
from tanner.sessions.session_analyzer import SessionAnalyzer

async def tes():
	r= await redis_client.RedisClient.get_redis_client()
	await r.set("jojo","test is done")

	
async def ge(ids):
	print(ids)
	r= await redis_client.RedisClient.get_redis_client()
	y= await r.get(str(id))
	#session= json.loads(y)
	#result = await SessionAnalyzer.create_stats(session, r)
	print(y)

def st(ids):
	print("getting the data as test")
	asyncio.run(tes())
	print("get func")
	asyncio.run(ge(ids))
st("jojo")

