import redis_client
import asyncio
import json
from tanner.sessions.session_analyzer import SessionAnalyzer

async def tes():
	r= await redis_client.RedisClient.get_redis_client()
	await r.set("jojo","test is done")

	
async def ge(id):
	r= await redis_client.RedisClient.get_redis_client()
	y= await r.get(id)
	session= json.loads(y)
	result = await SessionAnalyzer.create_stats(session, r)
	print(result)

def st(id):
	if __name__=="__main__":
		asyncio.run(tes())
		asyncio.run(ge(id))

