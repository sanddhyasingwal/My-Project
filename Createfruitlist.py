# Initialize an empty list to store the fruit names
fruit_list = []

# Loop to take input for 7 fruits
for i in range(7):
    fruit_name = input(f"Enter the name of fruit {i + 1}: ")
    fruit_list.append(fruit_name)

# Display the list of fruits
print("List of fruits:", fruit_list)
