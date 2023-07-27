import redis
import os
from decimal import Decimal, getcontext


pool = redis.ConnectionPool(
  host=os.getenv('REDIS_HOST', 'redis'),
  port=int(os.getenv('REDIS_PORT', 6379)),
  db=int(os.getenv('REDIS_DB', 0)))

r = redis.StrictRedis(connection_pool=pool)
getcontext().prec = 10000


def fibonacci(n: int):
  if n == 0:
    return 0
  elif n <= 2:
    return 1
  
  if r.exists(n):
    return Decimal(r.get(n))
  
  
  fib_sequence = [0, 1]
  
  # n以下の最も大きい連続するフィボナッチ数をredisから取得
  for i in range(n, 1, -1):
    if r.exists(i) and r.exists(i - 1):
      fib_sequence = [Decimal(r.get(i - 1).decode()), Decimal(r.get(i).decode())]
      break
  
  # n以下のフィボナッチ数を計算
  for i in range(len(fib_sequence), n + 1):
    fib_num = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(fib_num)
    r.set(i, str(fib_num))
  
  return fib_sequence[n]
  
  
if __name__ == '__main__':
  import sys
  
  if len(sys.argv) != 2:
    print('Usage: python fibonacci.py [n]')
  else:
    print(fibonacci(int(sys.argv[1])))
    