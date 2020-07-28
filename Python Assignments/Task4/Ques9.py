"""
Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
Example: If the limit is 3 , it should print:
0 EVEN
1 ODD
2 EVEN
3 ODD

"""

def showNumbers(limit):
    for num in range(limit+1):
        if num%2==0:
            print(num,"EVEN")
        else:
            print(num,"ODD")


user_input = input("Enter an integer: ")

showNumbers(int(user_input))