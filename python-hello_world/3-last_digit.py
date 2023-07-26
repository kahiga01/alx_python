#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
is_greater_than_5 = "and is greater than 5" if last_digit > 5 else ""
is_zero = "and is 0" if last_digit == 0 else ""
is_less_than_6 = "and is less than 6 and not 0" if last_digit < 6 and last_digit != 0 else ""

print("The string Last digit of", number, "is", last_digit, is_greater_than_5, is_zero, is_less_than_6)

