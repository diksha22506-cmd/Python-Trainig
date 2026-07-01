#program to analyze bank  transactions

#initalize variables
total_deposit = 0
total_withdrawal = 0
balance =0
while True:
    amount = float(input("Enter transaction amount (0 to stop): "))

    if amount == 0:
        break

    if amount > 0:
        total_deposit += amount
    else:
        total_withdrawal += abs(amount)

    balance += amount

print("\n----- Transaction Report -----")
print("Total Deposit:", total_deposit)
print("Total Withdrawal:", total_withdrawal)
print("Final Balance:", balance)