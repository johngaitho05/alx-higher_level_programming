#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    msg = 'is negative'
elif number == 0:
    msg = 'is zero'
else:
    msg = 'is positive'
print(f"{number} {msg}")
