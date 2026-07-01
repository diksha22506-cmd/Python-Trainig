#program to Count Prime Numbers in a Range 
start = int(input("Enter starting number: "))

# Accept the ending number from the user
end = int(input("Enter ending number: "))

# Variable to count total prime numbers
count = 0

print("Prime numbers are:")

# Loop through all numbers in the given range
for num in range(start, end + 1):

    # Prime numbers are greater than 1
    if num > 1:

        # Assume the number is prime
        is_prime = True

        # Check divisibility from 2 to num-1
        for i in range(2, num):

            # If divisible, it is not a prime number
            if num % i == 0:
                is_prime = False
                break

        # If the number is prime, print it and increase the count
        if is_prime:
            print(num)
            count += 1

# Display the total number of prime numbers
print("Total prime numbers =", count)