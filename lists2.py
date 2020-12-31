items=['apple','orange','melon']

print(items.index('orange',0,2)) # 1  starts from index 0

print(items.index('orange',2)) # ValueError: 'orange' is not in list

print('melon' in items) # True

print(items.count('orange')) # 1