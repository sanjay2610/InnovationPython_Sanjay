# Write a program in Python to iterate through the string “hello my name is Abcde” and print the string which has even length of the word.

sentence = 'hello my name is Abcde'

sentence = sentence.split(" ")
result=[]

for word in sentence:
    if len(word)%2==0:
        result.append(word)

print("Words with even length:", result)