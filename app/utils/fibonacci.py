def fibonacci(n: int):
  if n == 0:
    return 0
  elif n <= 2:
    return 1
  return fibonacci(n - 1) + fibonacci(n - 2)
