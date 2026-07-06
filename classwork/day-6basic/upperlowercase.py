# WAP to count uppercase and lowercase characters in a given sentence

sentence = input("Enter a sentence: ")

upper = 0
lower = 0

for x in sentence:
    if x >= 'A' and x <= 'Z':
        upper = upper + 1
    elif x >= 'a' and x <= 'z':
        lower = lower + 1

print("Uppercase letters =", upper)
print("Lowercase letters =", lower)