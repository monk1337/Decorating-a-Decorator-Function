def simple(func):
    def wrapper(xx):
        print("before the decorator")
        func(xx)
        print("after the decorator ")
    return wrapper


def New_func(x):
    print("calling this new function")

New_func=simple(New_func)
New_func(12)


#Instead of calling New_func=simple(New_func) we could use  @simple  which is called syntactic sugar

def simple(func):
    def wrapper(xx):
        print("before the decorator")
        func(xx)
        print("after the decorator ")
    return wrapper


@simple
def New_func(x):
    print("calling this new function")

New_func(12)
