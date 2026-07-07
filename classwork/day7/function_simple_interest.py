#function to calculate simple interest.
def calculate_simple_interest(Principal,rate,time):
    return(Principal*rate*time)/100
#---------------------------------------------------------
principal = float(input("Enter principal amount(in Rs):"))
rate = float (input("Enter rate of interest(in %)"))
time = float(input("Enter time period(in years):"))
print("Simple interest is Rs.",calculate_simple_interest(principal,rate,time))