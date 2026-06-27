# compund interest program
principal = float(input("enter the principal amount:"))
rate = float(input("enter the rate of interest"))
time = float(input("Enter Time (in years): "))

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print("Compound Interest =", compound_interest)
print("Total Amount =", amount) 