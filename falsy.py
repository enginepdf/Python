print(bool(None)) # False
print(bool([])) # False
print(bool({})) # False
print(bool(())) # False
print(bool('')) # False
print(bool(set())) # False
print(bool(range(0))) # False

print(None.__bool__()) # False
print(bool([].__len__())) # False