def my_function(*apple):
    print("the newest one is "+apple[1])

my_function("iphone7", 'ipad mini5')  #  the newest one is ipad mini5


def my_function2(**apple):
    print("the lastest one is "+ apple["ipad"])

my_function2(iphone="iphone7", ipad="ipad mini5") # the lastest one is ipad mini5
