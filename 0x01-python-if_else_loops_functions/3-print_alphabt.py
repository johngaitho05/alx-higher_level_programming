#!/usr/bin/python3
for i in range(97, 123):
    if "{:c}".format(i) not in "eq":
        print("{:c}".format(i), end="")
