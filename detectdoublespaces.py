def detect_double_spaces(input_string):
    if "  " in input_string:
        return True
    else:
        return False

# Example usage:
user_input = input("Enter a string: ")
if detect_double_spaces(user_input):
    print("Double spaces detected in the string.")
else:
    print("No double spaces found in the string.")

def replace_double_spaces(input_string):
    # Replace double spaces with a single space
    result_string = input_string.replace("  ", " ")
    return result_string

# Example usage:
user_input = input("Enter a string with double spaces: ")
result = replace_double_spaces(user_input)
print("String after replacing double spaces:", result)