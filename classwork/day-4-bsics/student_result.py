#program to analyze student result

n = int(input("Enter the number of students: "))

marks = []

# Accept marks of each student
for i in range(n):
    mark = float(input(f"Enter marks of Student {i + 1}: "))
    marks.append(mark)

# Calculate highest, lowest, and average marks
highest = max(marks)
lowest = min(marks)
average = sum(marks) / n

passed = 0
distinction = 0

# Count passed students and distinction holders
for mark in marks:
    if mark >= 40:
        passed += 1
    if mark >= 75:
        distinction += 1

print("\n----- Student Marks Report -----")
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Number of Students Passed:", passed)
print("Number of Students with Distinction:", distinction)