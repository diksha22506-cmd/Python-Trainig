# Simple interest program
principle = float(input("Enter the principal amount:"))
rate = float(input("Enter the rate of interest:"))
time = float(input("Enter the time in years:"))
simple_interest = (principle * rate * time) / 100
print("The simple interest is:", simple_interest)