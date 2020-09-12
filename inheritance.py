class State(): # State(object), State()
    secondhand=False


class Apple(State):
    def __init__(self, name, price):
        self.name = name
        self.price = price


Mac = Apple("Macbook", 2000)
Iphone = Apple("Iphone", 600)
Ipad = Apple("Ipad", 600)

# Find the oldest Apple
def most_expensive(*args):
    name=''
    max=0
    for item in args:
        if item.price > max:
            max=item.price
            name=item.name
    return name
    # return max(args)


# Output
print(f"{most_expensive(Mac, Iphone, Ipad)} is the most expensive one.")  # Macbook is the most expensive one.
print(isinstance(Mac, Apple)) # True
print(isinstance(Mac, State)) # True
print(Mac.secondhand) # False