if True:
    guess=10

print(guess) # 10

guess1=5
guess2=1
guess3=1

def guessing():
    guess1=20
    global guess2
    guess2=100
    return guess1

def guessing1(guess3):
    guess3*=10
    return guess3

print(guessing()) # 20
print(guess1) # 5
print(guess2) # 100
print(guessing1(guessing1(guessing1(guessing1(guessing1(guess3)))))) # 100000