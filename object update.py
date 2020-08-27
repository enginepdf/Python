
items = {
    12345:'number',
    'car': 'BMW',
    'driver': 'Ed Sheeran',
    'snacks': ['pringles', 'cola'],
    'is_on': True
}

print(items.keys()) # dict_keys([12345, 'car', 'driver', 'snacks', 'is_on'])

items.update({'is_on': False}) 
print(items) # {12345: 'number', 'car': 'BMW', 'driver': 'Ed Sheeran', 'snacks': ['pringles', 'cola'], 'is_on': False}

items['is_on'] = True
print(items) # {12345: 'number', 'car': 'BMW', 'driver': 'Ed Sheeran', 'snacks': ['pringles', 'cola'], 'is_on': True}

myitems = items.copy()
myitems.update({'car': None, 'driver': 'me'})
print(myitems) # {12345: 'number', 'car': None, 'driver': 'me', 'snacks': ['pringles', 'cola'], 'is_on': True}
print(items) # {12345: 'number', 'car': 'BMW', 'driver': 'Ed Sheeran', 'snacks': ['pringles', 'cola'], 'is_on': True}
print(myitems.get('money')) # None
print(myitems.get('money', 10000)) # 10000

newItems=dict(temp='number', car= 'Hyundai',
    driver= 'me',
    snacks= ['pringles', 'cola'],
    is_on= True)

print(newItems) # {'temp': 'number', 'car': 'Hyundai', 'driver': 'me', 'snacks': ['pringles', 'cola'], 'is_on': True}