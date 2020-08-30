for item in {'a','b','c'}:
    print(item) # b a c

for item in ('a','b','c'):
    print(item) # a b c
print(item) # c

items={'snack':'pringles', 'car':'BMW'}

for k, v in items.items():
    print(k,v) # snack pringles    car BMW

for val in items.values():
    print(val) # pringles, BMW

for key in items.keys():
    print(key) # snack, car