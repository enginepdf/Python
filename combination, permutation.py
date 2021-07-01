from itertools import permutations, product, combinations_with_replacement

data=['A','B','C']

result=list(permutations(data,3))
print(result) # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

result1=list(product(data, repeat=2)) # allow duplicate.   cartesian product, equivalent to a nested for-loop
print(result1) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

result2=list(combinations_with_replacement(data,2)) # choose 2, allow duplicate
result3=list(combinations_with_replacement(data,1))

print(result2) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
print(result3) # [('A',), ('B',), ('C',)]