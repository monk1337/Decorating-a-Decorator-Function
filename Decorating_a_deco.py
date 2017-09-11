def advance1(func):
    def simple1(func1):

        def wrapper1(xx):
            print("before the decorator")
            return func1(xx)
        return wrapper1
    return simple1

closure1=advance1(1)

def advance2(func2):
    def simple2(func3):
        def wrapper2(xx2):
            print("before the decorator2")
            return func3(xx2)

        return wrapper2
    return simple2

closure2=advance2(2)
closure2=closure1(closure2)


def new_func(sam):
    print("Life is Awesome")


new_func=closure2(new_func)
new_func(22)



# Instead of using many closures we could do same thing with pythonic way :


def advance1(func):
    def simple1(func1):

        def wrapper1(xx):
            print("before the decorator")
            return func1(xx)
        return wrapper1
    return simple1

@advance1(1)
def advance2(func2):
    def simple2(func3):
        def wrapper2(xx2):
            print("before the decorator2")
            return func3(xx2)

        return wrapper2
    return simple2

@advance2(2)


def new_func(sam):
    print("Life is Awesome")


new_func(22)
