def cmp(a, b):
    return (a > b) - (a < b) 

a = 100
b = 150
print(cmp(a, b)) # -1
  
a = 1
b = 1
print(cmp(a, b)) # 0
   
a = 150
b = 100
print(cmp(a, b)) # 1
print(100>150) # False
print(100<150) # True
print((100>150)-(100<150)) # -1
print((150>100)-(150<100)) # 1