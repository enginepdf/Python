num=10

while num<16:
    if num==12:
        break 
    print(num) # 10 11
    num +=1
else:
    print('while')
print('done') # done

while True:
    ans=input("To stop this, write 'quit' ") # 'quit' then while stops
    pass # go to next line
    if(ans=='quit'):
        break