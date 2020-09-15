numbers=[10,15,16]
products=['Chicken','Pizza','Dumpling']
quantities=(2,2,2)

def powerBy2(items): 
    result=[]
    for item in items:
        result.append(item**2)
    return result

def powerBy3(item):
    return item**3
 

def even(item):
    return item%2==0


print(powerBy2(numbers)) # [100, 225, 256]

print(list(map(powerBy3, numbers))) # [1000, 3375, 4096]

print(list(filter(even, numbers))) # [10, 16]

print(list(zip(products, quantities))) # [('Chicken', 2), ('Pizza', 2), ('Dumpling', 2)]

print(numbers) # [10, 15, 16]

