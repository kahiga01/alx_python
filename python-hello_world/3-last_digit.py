#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
is_positive = "positive" if number > 0 else ""
is_negative = "negative" if number < 0 else ""
is_zero = "zero" if number == 0 else ""

print("The string Last digit of", number, "is", last_digit, "and is", is_positive or is_negative or is_zero)

