# Program to create a list of 10 numbers and delete an element by position
numbers = []

# Input 10 numbers
print("Enter 10 numbers:")
for i in range(10):
    num = int(input("Enter number {i + 1}: "))
    numbers.append(num)

print("Original List:", numbers)

# Assign a position to delet an element from the list
position = int(input("Enter the position to delete: "))

# Check if position is valid
if position >= 0 and position < len(numbers):
    deleted = numbers.pop(position)
    print("Deleted element:", deleted)
    print("Updated List:", numbers)
else:
    print("Invalid position!")