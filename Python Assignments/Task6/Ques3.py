# Write a program to handle an error if the user entered the number more than four digits it should return 
# “Please length is too short/long !!! Please provide only four digits”

user_input = input("Enter a four digit number: ")

if user_input.isnumeric()==False or len(user_input)>4 or len(user_input)<4:
    raise Exception('Please length is too short/long !!! Please provide only four digits')