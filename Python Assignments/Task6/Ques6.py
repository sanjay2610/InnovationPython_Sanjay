"""
Read any file using Python File handling concept and return only the even length string from the doc.txt file.
Consider the content as: 
	Hello I am a file 
	Where you need to return the data string 
	Which is of even length 
	Make sure you return the content in 
	The same link as it is present.

"""

file = open("Python Assignments\Task6\doc.txt", "r")

words  = file.read()

words = (words.replace('\n','')).split(' ')

result=[]

for word in words:
    if len(word)%2==0:
        result.append(word)

print(result)