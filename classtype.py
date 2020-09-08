class newobj:
    pass

item=newobj()

print(type(item)) # <class '__main__.newobj'>


class items:
    def __init__(self, name):
        self.name=name
    
    def display(self):
        print(self.name)

item=items('earphone')
item.price=100
print(item.name) # earphone
item.display() # earphone
print(item.price) # 100