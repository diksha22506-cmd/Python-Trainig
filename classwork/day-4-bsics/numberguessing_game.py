# program to find the factors of a number
secret_number = 37

while True:
    guess = int(input("Enter your guess: "))

    if guess > secret_number:
        print("Too High")

    elif guess < secret_number:
        print("Too Low")

    else:
        print("Correct! You guessed the number.")
        break