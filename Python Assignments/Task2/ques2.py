"""
Write a program in Python to perform the following operator based task:
Ask the user to choose the following option first:
If User Enter 1 - Addition 
If User Enter 2 - Subtraction
If User Enter 3 - Division
If USer Enter 4 - Multiplication
If User Enter 5 - Average
Ask the user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
Ask the user to enter two more numbers as first1 and second2 for calculating the average as soon as the user chooses an option 5.
In the end, if the answer of any operation is Negative print a statement saying “Zsa”
NOTE: At a time users can perform one action at a time.

"""
print("Choose an option from the following alternatives: ")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")
print("5. Average")

userChoice=input("Enter the Option Number: ")
userChoice = int(userChoice)

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if userChoice==1:
    result = first+ second
    print(first, "+", second, "=", result)

elif userChoice==2:
    result = first - second
    print(first, "-",second, "=", result)

elif userChoice==3:
    result = first/second
    print(first, "/",second, "=", result)

elif userChoice==4:
    result = first * second
    print(first, "*",second, "=", result)

elif userChoice==5:
    third = int(input("Enter the third number: "))
    fourth = int(input("Enter the fourth number: "))
    result = (first+second+third+fourth)/4
    print("Average of ",first,second,third, fourth, "=", result)

else:
    print ("Invalid Choice Number Entered!")