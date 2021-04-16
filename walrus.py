# syntax := that assigns values to variables as part of a larger expression
# due to its resemblance to the eyes and tusks of a walrus.

# vi ~/.zshrc
#     alias python3=python3.8
#     :wq!
# source ~/.zshrc
# python -V
# python3 -V


item=['Notebook', 'Phone', 'Accessory']

while ((n := len(item)) >= 1):
    print(item)
    item.pop()

# ['Notebook', 'Phone', 'Accessory']
# ['Notebook', 'Phone']
# ['Notebook']