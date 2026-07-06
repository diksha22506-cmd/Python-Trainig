#wap to input a sentence and count the number of vowels present in it.
#input of sentence
sentence = input("Enter the sentence:")
#intialize vowel count as 0
vowels= 0
for x in sentence:
    if(x=='A' or x=='a' or x=='E'or x=='e'or x=='I'or x=='i'or x=='O'or x=='o'or x=='U'or x=='u'):
    #increment the vowel count
        vowels = vowels + 1
    print("The number of vowels in the sentence is:",vowels)