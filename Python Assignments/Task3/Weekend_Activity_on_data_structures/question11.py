""" 
Write a program to find out the occurrence of a specific word from an alphanumeric statement.
Example: 12abcbacbaba344ab  
Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic

"""

example  = '12abcbacbaba344ab'

buffer_list=[]

for n in example:
    if(n.isdigit()==False):
        buffer_list.append(n)

buffer_list = list(set(buffer_list))
buffer_list.sort()
result = {}

for x in buffer_list:
    result[x] = 0

for a in buffer_list:
    for n in example:
        if n==a:
            result[a] +=1

print(result)

