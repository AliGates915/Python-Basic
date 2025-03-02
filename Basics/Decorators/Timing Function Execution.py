import time

def timer(func):
  # pass the parameters which args are passed.
  def wrapper(*args, **kwargs):
    start = time.time()
    # Just func is execute. 
    res = func(*args, **kwargs) 
    end = time.time()
    print(f"{func.__name__} range in {end-start} time")
    return res
  return wrapper

@timer
def example(n):
  time.sleep(n)

example(2)