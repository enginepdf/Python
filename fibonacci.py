i=[-1]*50

def fibonacci(x):
    if x==1 or x==2:
        return 1
    
    if i[x]!=-1:
        return i[x]
    
    i[x]=fibonacci(x-1)+fibonacci(x-2)
    return i[x]

print(fibonacci(10)) # 55