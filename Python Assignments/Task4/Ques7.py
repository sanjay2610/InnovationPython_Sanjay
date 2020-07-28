# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have 
# the same length, then the function should print all strings line by line.

def srt_by_length(str1, str2):
    if (len(str1)>len(str2)):
        return str1
    elif(len(str1)<len(str2)):
        return str2
    else:
        return str1+'\n'+str2

str1 = input("Enter a string: ")
str2 = input("Enter another string: ")

result = srt_by_length(str1, str2)

print(result)