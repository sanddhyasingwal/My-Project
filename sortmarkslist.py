# Initialize an empty list to store the fruit names
sortedmarks_list = []

# Loop to take input for 6 numbers
for i in range(6):
    students_marks = int(input(f"Enter the marks {i + 1}: "))
    sortedmarks_list.sort()
    sortedmarks_list.append(students_marks)

# Display the list of fruits
print("Sorted marks of students:", sortedmarks_list)



