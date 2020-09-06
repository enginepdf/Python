from heapq import heappop, heappush, heapify

heap_tree=[]
items=[210,1,5,1000,50,79,120]

for item in items:
    heappush(heap_tree, item)

while heap_tree:
    print(heappop(heap_tree)) 
# 1
# 5
# 50
# 79
# 120
# 210
# 1000

heapify(items)
 
print(items) # [1, 50, 5, 1000, 210, 79, 120]  min-heap