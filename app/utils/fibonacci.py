from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n: int):
  if type(n) != int or n < 0:
    raise ValueError("Invalid input")
  
  if n == 0:
    return 0
  elif n <= 2:
    return 1
  return fibonacci(n - 1) + fibonacci(n - 2)
