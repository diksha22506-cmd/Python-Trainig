#wap to calculate the grade of student.
# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"


# Main Program
for i in range(1, 6):
    # Accept marks from the user
    marks = int(input(f"Enter marks of Student {i}: "))

    # Call the function
    grade = calculate_grade(marks)

    # Display result
    print("Marks:", marks)
    print("Grade:", grade)
    