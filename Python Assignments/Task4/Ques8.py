#   Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.

list1 = list(range(1,21))

result = tuple(list(n**2 for n in list1))

print(result)