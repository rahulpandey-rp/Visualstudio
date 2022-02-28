def replace_underscore(fn):
    def wrappers():
        result = fn()
        print("rep")
        return("_".join(result.split()))
    return(wrappers)


def convert_capital_case(fn):
    def wrappers():
        result = fn()
        print("sdhv")
        return(result.upper())
    return(wrappers)


@replace_underscore
@convert_capital_case
def greet():
    return('Welcome to Python')


print(greet())
