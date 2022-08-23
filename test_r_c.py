import asyncio
import logging 
import aioredis 

LOGGER= logging.getLogger(__name__)

class  R:
	@staticmethod
	async def get_r_c(poolsize=None):
		r_c=None
		try:
			host ="localhost"
			port =6379
			uname=""
			passw=""
			if poolsize is None:
				poolsize=80
			r_c = aioredis.from_url(f"redis://{uname}:{passw}@{host}:{port}",encoding="utf-8",decode_responses=True,ma_connections=poolsize)
		except asyncio.TimeoutError as timeout_error:
			LOGGER.exception("afasdfasdfsdf" timeout_error)
			exit()
		return r_c
		
		
