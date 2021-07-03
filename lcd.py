import math

def lcm(a,b):
    return a*b // math.gcd(a,b)

a=30
b=60

print(math.gcd(a,b)) # 30
print(lcm(a,b)) # 60