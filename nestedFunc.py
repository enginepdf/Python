def multiply(a,b):
    def calculate(c,d):
        return c*d
    return calculate(a,b)
    print("This doesn't get printed")

check=multiply(10,5)
print(check) # 50
