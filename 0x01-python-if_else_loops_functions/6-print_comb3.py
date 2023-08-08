#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (j * 10 + i) < (i * 10 + j) or i == j:
            continue
        if (i * 10 + j) != 89:
            print(('0' if (i * 10 + j) < 10 else '') + str(i * 10 + j), end=', ')
print(89)
