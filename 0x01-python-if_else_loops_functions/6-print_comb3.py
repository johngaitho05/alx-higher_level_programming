#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (j * 10 + i) < (i * 10 + j) or i == j:
            continue
        elif (i * 10 + j) == 89:
            print('{num}'.format(num=89))
        elif (i * 10 + j) < 10:
            print("{prefix}{num}".format(num=(i * 10 + j), prefix='0'), end=', ')
        else:
            print("{num}".format(num=(i * 10 + j)), end=', ')

