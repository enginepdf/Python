foods=['noodle','meat','vegetables','#']

foods[3]='eggs'

lists=foods
lists[0]='fruits'

wishes=foods[0:2]
wishes[0]='sauces'

print(foods) # ['fruits', 'meat', 'vegetables', 'eggs']
print(lists) # ['fruits', 'meat', 'vegetables', 'eggs']
print(wishes) # ['sauces', 'meat']