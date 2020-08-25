foods=['noodle','meat','vegetables','#']

foods.pop() # foods.remove('#')
foods.insert(3,'eggs')
foods.extend(['ice cream','fishes'])

lists=foods
lists[0]='fruits'

wishes=foods[0:2]
wishes[0]='sauces'

sliced=foods[:]
sliced[0]='sauces'

print(foods) # ['fruits', 'meat', 'vegetables', 'eggs', 'ice cream', 'fishes']
print(lists) # ['fruits', 'meat', 'vegetables', 'eggs', 'ice cream', 'fishes']
print(wishes) # ['sauces', 'meat']
print(sliced) # ['sauces', 'meat', 'vegetables', 'eggs', 'ice cream', 'fishes']