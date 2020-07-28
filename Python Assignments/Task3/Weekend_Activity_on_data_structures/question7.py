# Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the string with their index.

example="Hello World"

print(example[::-1])

vowels = ['a','e', 'i', 'o', 'u']
result=[]

for x in example:
    if x in vowels:
        result.append(x)

print("Vowels in the string", set(result))



