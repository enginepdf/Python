# Reference : https://medium.com/python-features/understanding-if-name-main-in-python-a37a3d4ab0c3

def check():
    name = "John"
    print(f"he/she is {name}")
print("top-level in person module")

if __name__ == "__main__": # __name__ attribute will be set to __main__
    print("person mod is run directly")
else:
    print("person mod is imported into another module")

# top-level in person module
# person mod is run directly