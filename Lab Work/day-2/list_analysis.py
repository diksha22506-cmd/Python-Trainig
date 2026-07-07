# Function to find the maximum number
def find_max(numbers):
    return max(numbers)


# Function to find the minimum number
def find_min(numbers):
    return min(numbers)


# Function to find the average
def find_average(numbers):
    return sum(numbers) / len(numbers)


# Main Program
numbers = []

# Accept 10 integers from the user
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Call the functions
maximum = find_max(numbers)
minimum = find_min(numbers)
average = find_average(numbers)

# Display the results
print("\nList:", numbers)
print("Maximum Value:", maximum)
print("Minimum Value:", minimum)
print("Average:", average)