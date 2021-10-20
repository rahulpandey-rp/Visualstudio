def check_value(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args)
        return(f"sum is {result}")
    return(wrapper)


@check_value
def sum_val(*args):
    return(sum(args))


def sum_v(*args):
    return(sum(args))


print(sum_val(2, 3))
sum_val2 = check_value(sum_v)
print(sum_val2(2, 3))
