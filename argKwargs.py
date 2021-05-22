def my_function(*apple):
    print(type(apple)) # <class 'tuple'>     positional arguments
    print("the newest one is "+apple[1])

my_function("iphone7", 'ipad mini5')  #  the newest one is ipad mini5


def my_function2(**apple):
    print(type(apple)) # <class 'dict'>      keyword arguments
    print("the lastest one is "+ apple["ipad"])

my_function2(iphone="iphone7", ipad="ipad mini5") # the lastest one is ipad mini5