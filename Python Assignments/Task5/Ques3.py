# Write a program to Python find out the character in a string which is uppercase using list comprehension.
sample_string = 'Hello World!'

result = [x for x in sample_string if x.isupper()]

print(result)