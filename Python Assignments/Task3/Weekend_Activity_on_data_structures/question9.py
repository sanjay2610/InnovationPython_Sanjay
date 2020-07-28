# Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.
from itertools import combinations

x=[1,2,3,4,5,6,7,8,9,-1]

comb= combinations(x, 2)
result=[]

for x, y in comb:
    if(x+y==8):
        bufferlist=[x,y]
        result.append(bufferlist)

print(result)




