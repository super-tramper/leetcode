import functools
import time


def log(a):
    def wrapper(*args, **kwargs):
        print('%s' % time.time())
        return a()
    return wrapper


@log
def test():
    print('a')

test()
