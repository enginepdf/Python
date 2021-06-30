from collections import Counter

counter=Counter(['a','a','b'])

print(counter['a']) # 2
print(counter['b']) # 1
print(dict(counter)) # {'a': 2, 'b': 1}