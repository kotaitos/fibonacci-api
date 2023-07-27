import redis
import os


pool = redis.ConnectionPool(
  host=os.getenv('REDIS_HOST', 'redis'),
  port=int(os.getenv('REDIS_PORT', 6379)),
  db=int(os.getenv('REDIS_DB', 0)))

r = redis.StrictRedis(connection_pool=pool)


def fibonacci(n: int):
  if n == 0:
    return 0
  elif n <= 2:
    return 1
  
  if r and r.exists(n):
    return int(r.get(n))
  
  result = fibonacci(n - 1) + fibonacci(n - 2)
  
  if r:
    r.set(n, result)
  
  return result
