# Decorating-a-Decorator-Function
Let's decorate a decorator function


You have seen a python decorator :

Simple Decorator :

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


But have you tried decorating a decorator ? Let's try 
