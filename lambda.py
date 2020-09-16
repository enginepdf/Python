items=[10,20,30]

foods=[('chicken',1,5000),('ham',10,50000),('pizza',3,30000)]


print(list(map(lambda item: item**3, items))) # [1000, 8000, 27000]
print(list(filter(lambda item: item%10 ==0, items))) # [10, 20, 30]
foods.sort(key=lambda x:x[2])
print(foods) # [('chicken', 1, 5000), ('pizza', 3, 30000), ('ham', 10, 50000)]