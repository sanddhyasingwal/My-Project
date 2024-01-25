# Take input of 4 numbers from users
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

# Find the greatest number using if-else statements
if num1 >= num2 and num1 >= num3 and num1 >= num4:
    greatest_number = num1
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    greatest_number = num2
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    greatest_number = num3
else:
    greatest_number = num4

# Display the greatest number
print(f"The greatest number among {num1}, {num2}, {num3}, and {num4} is: {greatest_number}")
