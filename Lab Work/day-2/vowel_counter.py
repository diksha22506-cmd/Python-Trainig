# Function to count vowels
def count_vowels(text):
    count = 0

    for ch in text:
        if ch.lower() in "aeiou":
            count += 1

    return count


# Main Program
sentence = input("Enter a sentence: ")

total = count_vowels(sentence)

print("Total Vowels:", total)