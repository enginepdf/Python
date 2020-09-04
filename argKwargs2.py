def pam(name, *args, test='test',**kwargs):
    total=0
    print(sum(args)) # 6
    print(kwargs) # {'item1': 2, 'item2': 12}
    print(name) # Andy
    print(test) # test
    for item in kwargs.values():
        total+=item
    return sum(args)+total 

print(pam('Andy',1,2,3,item1=2, item2=12)) # 20