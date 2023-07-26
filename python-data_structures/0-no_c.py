def no_c(my_string):
    result = ''
    for char in my_string:
        if char.lower() != 'c':
            result += char
    return result

# Test the function
input_string = "Can you C me now?"
output_string = no_c(input_string)
print(output_string)  # Output: "an you  me now?"

