data=list(range(0,10))

print(data) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for idx, val in enumerate(data):
    if val==2:
        print(f'index {idx}')
    print(idx, val)

# 0 0
# 1 1
# index 2
# 2 2
# 3 3
# 4 4
# 5 5
# 6 6
# 7 7
# 8 8
# 9 9