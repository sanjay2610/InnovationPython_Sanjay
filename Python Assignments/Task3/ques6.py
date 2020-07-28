#Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
import math
list1 = list(range(1,31))
print(list1)

first5 = list1[0:5]
last5 = list1[-5:]

bufferlist = first5+last5
result=[]

for n in bufferlist:
    result.append(n**2)

print(result)




