def add(*args):
    return(sum(args))


def catch(fn=add, *args, **kwargs):
    kwargs["result"] = str(kwargs["c"]) + " " + str(add(*args))
    result = fn(*args)
    print(f"Args: {','.join(map(str,args))}")
    print(*('='.join(item) for item in kwargs.items()))
    print(f"Result: {kwargs['c']} {result}")


catch(add, 1, 2, c="this is sum")
