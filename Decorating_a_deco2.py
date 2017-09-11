# See the difference between first file : decorating_a_deco and this file :
# In this file the second deco is not having extra outer function


def advance1(func):
    def simple1(func1):

        def wrapper1(xx):
            print("before the decorator")
            return func1(xx)
        return wrapper1
    return simple1

@advance1(1)
def advance2(func2):
    def simple22(xx3):
        print("after deco1")
        return func2(xx3)
    return simple22

@advance2



def new_func(sam):
    print("Life is Awesome")


new_func(22)
