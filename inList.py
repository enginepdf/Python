items=['a','a','b','b','b']

result=[]

for item in items:
    if item not in result:
        result.append(item)
print(result) # ['a', 'b']