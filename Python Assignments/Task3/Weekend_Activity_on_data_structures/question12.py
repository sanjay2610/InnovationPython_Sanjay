# Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

example = (1,2,3,4,5,6,7,8,9,10)

buffer_list = [num for num in example if num%2==0]

result = tuple(buffer_list)

print(result)