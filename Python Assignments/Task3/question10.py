#Write a program which accepts a sequence of comma-separated numbers from the console and generate a list and a tuple which contains every number. 

user_input = input("Enter a list of numbers seperated by comma like '1,2,3' :")

user_input = user_input.split(',')

print("List:", user_input)
print("Tuple: ", tuple(user_input))
