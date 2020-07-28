"""
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
Hints: Use map() to generate a list.
     	Use filter() to filter elements of a list
        Use lambda to define anonymous functions

"""

def square(num):
    return num**2

def list_filter(list1):
    result = filter(lambda x: (x%2==0), list1)
    return list(result)

sample_list = [1,2,3,4,5,6,7,8,9,10]

sample_list = list_filter(sample_list)

sample_list = list(map(square, sample_list))

print(sample_list)