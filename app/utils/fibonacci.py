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
  
  if r.exists(n):
    return int(r.get(n))
  
  
  fib_sequence = [0, 1]
  
  # n以下の最も大きい連続するフィボナッチ数をredisから取得
  found_index = 1
  for i in range(n, 1, -1):
    if r.exists(i) and r.exists(i - 1):
      fib_sequence = [int(r.get(i - 1)), int(r.get(i))]
      found_index = i
      break
  
  # n以下のフィボナッチ数を計算
  for i in range(n - found_index):
    fib_num = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(fib_num)
    r.setnx(found_index + i + 1, int(fib_num))
  
  return fib_sequence[-1]
  
  
if __name__ == '__main__':
  import sys
  
  if len(sys.argv) != 2:
    print('Usage: python fibonacci.py [n]')
  else:
    print(fibonacci(int(sys.argv[1])))
