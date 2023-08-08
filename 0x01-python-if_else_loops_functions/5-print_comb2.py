#!/usr/bin/python3
for i in range(0, 99):
    print('0{i}, '.format(i=i) if i < 10 else '{i}, '.format(i=i), end='')
print(99)
