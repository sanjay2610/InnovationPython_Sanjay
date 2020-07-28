"""
Write a program in Python to perform the following operation:
If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “c” as a string
If a number is divisible by both 3 and 5 its should print “Consultadd Python Training” as a string.

"""

userinput= input("Enter a number: ")
userinput = int(userinput)

if (userinput%3==0 and userinput%5==0):
    print(userinput, "is divisible by both 3 & 5")
elif userinput%3==0 and not userinput%5==0:
    print(userinput, "is only divisible by 3")
elif userinput%5==0 and not userinput%3==0:
    print(userinput, "is only divisible 5")