# Write a program in Python to  multiple the element of list by itself using a traditional function and 
# pass the function to map to complete the operation.

def square(num):
    return num**2

sample_list=list(range(1,11))

sample_list = list(map(square, sample_list))

print(sample_list)