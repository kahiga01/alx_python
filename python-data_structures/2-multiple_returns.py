def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return length, first_char

# Test the function
sentence1 = "Hello, World!"
result1 = multiple_returns(sentence1)
print(result1)  # Output: (13, 'H')

sentence2 = ""
result2 = multiple_returns(sentence2)
print(result2)  # Output: (0, None)

