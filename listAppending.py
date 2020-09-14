class cart(list):
  def __init__(self, market):
      self.market=market

food_cart = cart("E-mart");

food_cart.append("ham")
food_cart.append("chicken")
print(food_cart.market) # E-mart
print(food_cart) # ['ham', 'chicken']
print(issubclass(cart, list)) # True