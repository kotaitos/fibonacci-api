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
  
  fib_sequence = [0, 1]
  for i in range(2, n + 1):
    fib_num = fib_sequence[i - 1] + fib_sequence[i - 2]
    fib_sequence.append(fib_num)
  
  if r:
    r.set(n, fib_sequence[n])
  
  return fib_sequence[n]
