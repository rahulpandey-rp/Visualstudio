'''
tp = ([20,22],[21,22])
tp[0][1] = 23

def hello():
    pass

print(hello())

#reduce
no_input  = input()

list_int = list(no_input.split())
print(list_int)

list_no = [2,3,4,5, None,6, None]

print(list(filter(lambda x: x is not None, list_no)))

def decorator(arg):
    def define(fn):
        def wrappers():
            print(arg)
            print("Hi am decorator")
            sn = fn()
        return wrappers
    return define


@decorator("Hey")
def info():
    print("Hello world")

info()
#overridig/ overloading

class Child:
    def __init__(self):
        pass
    def add(self):
        pass

st1 = Child()
st1.add()


Child.__add__(st1)'''