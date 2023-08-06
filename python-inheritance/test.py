#!/usr/bin/python3
from is_same_class import is_same_class

a = 1
print(is_same_class(a, int))  # Correct output: True

a = True
print(is_same_class(a, int))  # Correct output: False

a = True
print(is_same_class(a, object))  # Correct output: False

a = None
print(is_same_class(a, object))  # Correct output: True

a = None
print(is_same_class(a, list))  # Correct output: False

a = [1, 2, 3]
print(is_same_class(a, list))  # Correct output: True

a = [1, 2, 3]
print(is_same_class(a, object))  # Correct output: False

