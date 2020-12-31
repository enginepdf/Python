items=[item for item in 'apple']

print(items) # ['a', 'p', 'p', 'l', 'e']

items1=[item for item in 'apple' if item=='a']

print(items1) # ['a']

set1={item for item in 'apple'}

print(set1) # {'e', 'a', 'p', 'l'}


menu={'chicken':12000,'pizza':10000}
myorder={name:price*3 for name,price in menu.items()  if name=='chicken'}
print(myorder) # {'chicken': 36000}

new={'Apple':item+'10' for item in ['iphone']}
print(new) # {'Apple': 'iphone10'}