import time
from functools import wraps


def log_it(fn):
    @wraps(fn)
    def wrappers(*args, **kwargs):
        print(f"The name of function is {fn.__name__}")
        print(f"The args are {args} \nThe kwargs are {kwargs}")
        time_start = time.time()
        print(fn(*args, **kwargs))
        time_stop = time.time()
        print(
            f"The time taken to execute the function is {time_stop-time_start}"
            )
    return(wrappers)


@log_it
def check(*args, **kwargs):
    pass


check(2, "hey", "hellow", 4, 6, Name='Rahul', No=5248)
