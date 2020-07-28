#Write a program that accepts a string as an input from the user and calculates the number of digits and letters.


user_input = input("Enter a Alphnumeric string: ")

letters = 0
digits = 0

for x in user_input:
    if (x.isdigit()):
        digits +=1
    else:
        letters+=1

print("Number of letters: ", letters)
print("Number of digits: ", digits)