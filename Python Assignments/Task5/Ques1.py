# Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7. 
# Make sure to use only higher order function.

def div_3(num):
    if num%3==0:
        return True
    else: 
        return False

def mul_7_not_div_3(num):
    if num%7==0 and div_3(num)==False:
        return True
    else: 
        return False

sample = [7,14,21,28,31]

for num in sample:
    if mul_7_not_div_3(num):
        print(num)

