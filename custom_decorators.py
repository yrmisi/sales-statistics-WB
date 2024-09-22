from functools import wraps
from time import time


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start: float = time()
        result = func(*args, **kwargs)
        end: float = time()
        print(f"\nФункция '{func.__name__}' выполнена за {end - start:.3f} сек")
        return result

    return wrapper
