def binary_search(array, target, start, end):
    while start<=end:
        mid=(start+end)//2

        if array[mid]==target:
            return mid

        elif array[mid]>target:
            end=mid-1
        
        else:
            start=mid+1
    return None

item=[1,2,3,4,5,6,7,10,15]
print(binary_search(item,6,0,len(item)-1)) # 5