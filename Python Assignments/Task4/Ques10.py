# Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)
def list_filter(list1):
    result = filter(lambda x: (x%2==0 and x<=20 and x>=1), list1)
    return list(result)

sample_list = [1,2,3,4,5,20,21,22,24]

sample_list = list_filter(sample_list)

print(sample_list)