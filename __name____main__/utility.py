# Reference : https://medium.com/python-features/understanding-if-name-main-in-python-a37a3d4ab0c3

import person
person.check()

if __name__ == "__main__": # __name__ attribute for person module will be set to “person” itself, while __name__ of the utility module will be set to __main__
    print("utility mod is run directly")
else:
    print("utility mod is imported into another module")


# top-level in person module
# person mod is imported into another module
# he/she is John
# utility mod is run directly