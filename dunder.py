class Apple:
    def __init__(self, name, price):
        self.name=name
        self.price=price
        self.description={
            'guarantee':'1 year',
            'copyright':'reserved'
        }

    def __call__(self,day):
        print(f'in {day} days, it will be shipped')


    def __del__(self):
        print('order done')

    
    def __getitem__(self, i):
        return self.description[i]


Iphone=Apple('Iphone XS',700)

Iphone(3) # in 3 days, it will be shipped
print(Iphone['guarantee']) # 1 year
del Iphone # order done