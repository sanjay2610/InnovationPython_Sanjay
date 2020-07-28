# Define a function that can receive two integral numbers in string form and compute their sum and print it in console.

def cal_sum(num1, num2):
    num1 = int(num1)
    num2 = int(num2)

    return num1+num2

num1= input("Enter an interger: ")
num2= input("Enter second integer: ")

print("Sum of the two numbers =", cal_sum(num1, num2))