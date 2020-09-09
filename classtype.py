class newobj:
    pass

item=newobj()

print(type(item)) # <class '__main__.newobj'>


class items:
    guarantee=True
    def __init__(self, name, quantity):
        if self.guarantee: # items.guarantee
            self.name=name
            self.quantity=quantity
    
    def display(self):
        print(self.name)

    @classmethod
    def order(cls, q):
        return cls('Iphone11',q)

    @staticmethod
    def check(q):
        print (f'do you want to order {q} item(s)?')

item=items('earphone',1)
item.price=100
print(item.name) # earphone
item.display() # earphone
print(item.price) # 100

print(item.guarantee) # True
item2=items.order(1)
print(item2.name) # Iphone11
print(item2.quantity) # 1

item2.check(1) # do you want to order 1 item(s)?
items.check(2) # do you want to order 2 item(s)?