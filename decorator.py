def decorator_function(func):

    def inner_func():
        print("First")

        func()

    return inner_func

def test():
    print("Second")

test() # Second

test1 = decorator_function(test)

test1() # First Second


@decorator_function
def test2():  
    print("Third")

test2() # First Third