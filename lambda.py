items=[10,20,30]

print(list(map(lambda item: item**3, items))) # [1000, 8000, 27000]
print(list(filter(lambda item: item%10 ==0, items))) # [10, 20, 30]