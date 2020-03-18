from datetime import datetime


def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        # result = func(*args, **kwargs)
        end = datetime.now()
        print(func.__qualname__, args, "took \t\t",
            (end-start).total_seconds() * 1000, "miliseconds")
        return result
    return wrapper


def timer_noresult(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = list(func(*args, **kwargs))
        # result = func(*args, **kwargs)
        end = datetime.now()
        # print(func.__qualname__, args, "took \t\t",
        #       (end-start).microseconds/1000, "milliseconds")
        return (end-start).total_seconds() * 1000
    return wrapper
