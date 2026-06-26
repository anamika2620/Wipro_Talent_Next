
# Dictionary storing student records
students = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

# User enters student name
name = input("Enter a name: ")

# Get marks list
marks = students[name]

# Calculate average
average = sum(marks) / len(marks)

# Print result
print("Average percentage mark:", average)
