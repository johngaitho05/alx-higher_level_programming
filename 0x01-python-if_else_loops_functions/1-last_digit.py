#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[-1]
if int(last_digit) > 5:
    msg = 'and is greater than 5'
elif int(last_digit) == 0:
    msg = 'and is 0'
else:
    msg = 'and is less than 6 and not 0'
print(f"Last digit of {number} is {last_digit} {msg}")
