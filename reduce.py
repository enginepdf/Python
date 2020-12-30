from functools import reduce

number1=[10,11,12]
number2=[100,200,300]


def accumulator(acc, item):
    return acc+item

print(reduce(accumulator,(number1+number2),0)) # 633
print(number1) # [10, 11, 12]

print(reduce(lambda acc, cur:acc*cur,number2,2)) # 12000000  result:acc*result