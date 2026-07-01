#program to analyze electricity bill
n = int(input("Enter the number of houses: "))

# Read the units consumed by each house
units = []

for i in range(n):
    unit = float(input(f"Enter electricity units consumed by House {i + 1}: "))
    units.append(unit)

# Calculate total units
total = sum(units)

# Calculate average units
average = total / n

# Find highest and lowest consumption
highest = max(units)
lowest = min(units)

# Display the results
print("\n----- Electricity Consumption Report -----")
print("Total Units Consumed:", total)
print("Average Units Consumed:", average)
print("Highest Consumption:", highest)
print("Lowest Consumption:", lowest)