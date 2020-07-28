#Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and a multiple of 2.

def div3(num):
    if num%3==0:
        return True
    else:
         return False

def div2(num):
    if num%2==0:
        return True
    else:
         return False


numbers = list(range(1,100))
result=[]

for number in numbers:
    if div2(number) and div3(number):
        result.append(number)

print(result)
