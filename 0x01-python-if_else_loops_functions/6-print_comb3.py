#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (j * 10 + i) < (i * 10 + j) or i == j:
            continue
        elif (i * 10 + j) == 89:
            print('{num}'.format(num=89))
        else:
            print("{prefix}{num}"
                  .format(num=(i * 10 + j), prefix='0' if (i * 10 + j) < 10 else ''), end=', ')
