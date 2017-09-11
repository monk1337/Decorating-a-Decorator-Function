def advance(func):
    def simple(func1):

        def wrapper(xx):
            print("before the decorator")
            func1(xx)
            print("after the decorator ")
        return wrapper
    return simple

Closure1=advance(1)

def New_func(x):
    print("calling this new function")

New_func=Closure1(New_func)
New_func(12)



#Instead of calling New_func=Closure1(New_func)  we could use 


def advance(func):
    def simple(func1):

        def wrapper(xx):
            print("before the decorator")
            func1(xx)
            print("after the decorator ")
        return wrapper
    return simple

@advance(1)
def New_func(x):
    print("calling this new function")

New_func(12)
