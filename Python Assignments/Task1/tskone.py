#1.	Create three variables in a single line and assign different values to them and make sure their data types are different. 
# Like one is int, another one is float and the last one is a string.

a,b,c = 4, 4.421, "innovation"

#2. Create a variable of value type complex and swap it with another variable whose value is an integer.

c = 1+2j
print(c)
d = 1

c= d
print(c)

# Swap two numbers using the third variable as the result name and do the same task without using any third variable.
x="One"
y="Two"

z=x
x=y
y=z


print("x:",x)
print("y:", y)

m, n="one", "two"
m,n=n,m

print("m:", m)
print("n:",n)


#python 2 syntax: This function reads the avery input as a string
# python2input = raw_input("Enter your name: ")

# print(python2input)

#python3 syntax: this also stores the value as a string
python3input= input("Enter a number between 1 and 10: ")
input1= input("Enter another number between 1 and 10: ")

python3input = int(python3input)
input1 = int(input1)

print(python3input, input1)

if (python3input <1 or input1 < 1 or python3input>10 or input1>10):
    raise Exception("Invalid Value Entered!")
else:
    result= python3input+input1+30
    print("Final Result:", result)

#6. 	Write a program to check the data type of the entered values. 
# HINT: Printed output should say -  The input value data type is: int/float/string/etc

from ast import literal_eval

input_data = input("Enter a int/float/string: ")

try:
    print( type(literal_eval(input_data)))
except (ValueError, SyntaxError):
        # A string, so return str
        print ("String")

""" 
If one data type value is assigned to ‘a’ variable and then a different data type value 
is assigned to ‘a’ again. Will it change the value. If Yes then Why? 

Yes, the value change as Python is a synamically typed language.  Dynamic typed programming 
languages are those languages in which variables must necessarily be defined before they are 
used. This implies that dynamic typed languages do not require the explicit declaration of 
the variables before they're used.  Python interpreter does type checking only as code runs, 
and the type of a variable is allowed to change over its lifetime

 """
