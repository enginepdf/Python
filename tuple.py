tuple=(1,2,3)
a, *rest=tuple

print(a) #1
print(rest) #[2,3]
print(tuple.count(2)) #  1
print(tuple.index(1)) # 0
print(len(tuple)) # 3

print(1 in tuple) # True

items={
    ('snack','icecream'):['pringles', 'baskin rabins'],
}
print(items[('snack','icecream')]) # ['pringles', 'baskin rabins']