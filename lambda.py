items=[10,20,30]

foods=[('chicken',2,10000),('ham',10,5000),('pizza',3,10000)] # (name, quantitiy, price per unit)


print(list(map(lambda item: item**3, items))) # [1000, 8000, 27000]
print(list(filter(lambda item: item%10 ==0, items))) # [10, 20, 30]
foods.sort(key=lambda x:x[1]*x[2], reverse=True)
print(foods) # [('ham', 10, 5000), ('pizza', 3, 10000), ('chicken', 2, 10000)]