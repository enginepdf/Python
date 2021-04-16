x = 1   # global

def outer():
    x = 2
    def inner():
        nonlocal x
        x = 3
        print("inner is ", x) # inner is  3
    inner()
    print("outer is ", x) # outer is  3
outer()

print("global is ", x) # global is  1

def func():
    nonlocal x  # nonlocal only for nested function
    x = 2
    print("x is ", x)
func()
print("global is ", x) # SyntaxError: no binding for nonlocal 'x' found