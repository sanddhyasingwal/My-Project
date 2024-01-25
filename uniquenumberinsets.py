# Initialize an empty set to store unique numbers
unique_numbers = set()

# Take input of 8 numbers from users
for i in range(8):
    user_input = int(input(f"Enter number {i + 1}: "))

    # Add the number to the set
    unique_numbers.add(user_input)

# Display the unique numbers
print("Unique numbers entered by the user:")
for number in unique_numbers:
    print(number)
