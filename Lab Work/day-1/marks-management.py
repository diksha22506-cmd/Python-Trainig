# Student Marks Management

students = {}

# Input marks of 5 students
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# Display all students
print("\nStudent Names and Marks:")
for name in students:
    print(name, ":", students[name])

# Add a new student
name = input("\nEnter new student name: ")
marks = int(input("Enter marks: "))
students[name] = marks

print("\nAfter Adding Student:")
for name in students:
    print(name, ":", students[name])

# Update marks of an existing student
name = input("\nEnter student name to update marks: ")

if name in students:
    marks = int(input("Enter new marks: "))
    students[name] = marks
    print("Marks Updated Successfully.")
else:
    print("Student not found.")

print("\nAfter Updating Marks:")
for name in students:
    print(name, ":", students[name])

# Delete a student
name = input("\nEnter student name to delete: ")

if name in students:
    del students[name]
    print("Student Deleted Successfully.")
else:
    print("Student not found.")

print("After Deleting Student:")
for name in students:
    print(name, ":", students[name])

# Display student with highest marks
highest_student = ""
highest_marks = -1

for name in students:
    if students[name] > highest_marks:
        highest_marks = students[name]
        highest_student = name

print("\nStudent with Highest Marks:")
print(highest_student, ":", highest_marks)