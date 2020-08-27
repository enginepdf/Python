set_items={1,2,2,3,20,20,30,50,25}

print(set_items) # {1, 2, 3, 50, 20, 25, 30}

set_items.add(23)

print(set_items) # {1, 2, 3, 50, 20, 23, 25, 30}

items=[1,2,2,3,20,20,30,50,25]

set_i=set(items)

print(set_i) # {1, 2, 3, 50, 20, 25, 30}

print(len(set_i)) # 7

print(1 in set_i) # True

print(list(set_i)) # [1, 2, 3, 50, 20, 25, 30]

newSet=set_i.copy()
set_i.clear()
print(newSet) # {1, 2, 3, 50, 20, 25, 30}
print(set_i) # set()



set1={1,2,3,4,5,6,7,8,9,10}
set2={7,8,9,10,11}


print(set1.intersection(set2)) # {8, 9, 10, 7}
print(set1 & set2) # {8, 9, 10, 7}

print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
print(set1 | set2) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

print(set1.difference(set2)) # {1, 2, 3, 4, 5, 6}
set1.difference_update(set2)
print(set1) # {1, 2, 3, 4, 5, 6}
print(set1.isdisjoint(set2)) # True

setA={1,2}
setB={1,2,3}
print(setA.issubset(setB)) # True
print(setB.issuperset(setA)) # True


setB.discard(3)
print(setB.pop()) # 1
print(setB) # {2}




