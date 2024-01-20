# Author : Sanddhya
# Program for Calculator

num1 = int(input("Enter first Number : "))
num2 = int(input("Enter second Number : "))

print(type(num1))
print(type(num2))

Operation = input("Enter your operator (+,-,*,/,%) ")

if Operation == "+":
    print(num1+num2)
elif Operation == "-":
    print(num1-num2)
elif Operation == "*":
    print(num1*num2)
elif Operation == "/":
    print(num1/num2)
elif Operation == "%":
    print(num1 % num2)
else:
    print(" The operation cannot be performed")

