def recursive(i):
    if i==10:
        return
    print('on',i)
    recursive(i+1)
    print('off',i)

recursive(1)

# on 1
# on 2
# on 3
# on 4
# on 5
# on 6
# on 7
# on 8
# on 9
# off 9
# off 8
# off 7
# off 6
# off 5
# off 4
# off 3
# off 2
# off 1