from time import time


def timer(f):
    def merti(*args, **kwargs):
        before = time()
        timed = f(*args, **kwargs)
        after = time()
        print("time elapsed: ", str(after - before))
        return timed
    return merti


def ntimes(n):
    def inner(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                ntimed = func(*args, **kwargs)
                print('performing: {.__name__}'.format(func))
            return ntimed
        return wrapper
    return inner


@ntimes(3)
def add(x, y):
    return x+y


print(add(5, 6))
timer(add(3, 6))
