def check_iter(iterable):
    try:
        iter(iterable)
    except TypeError:
        print(f"{type(iterable)} Object is not iterable")
    else:
        print(f"{type(iterable)} Object is iterable")


iterable = 132
check_iter(iterable)
