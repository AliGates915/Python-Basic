import time

def cache(func):
  cache_value = {}
  print(cache_value)
  def wrapper(*args):
    if args in cache_value:
      return cache_value[args]
    res = func(*args)
    cache_value[args] = res
    return res
  return wrapper

@cache
def long_run(a , b):
  time.sleep(4)
  return a + b

print(long_run(2,5))
print(long_run(7,5))
print(long_run(3,2))
print(long_run(4,1))
