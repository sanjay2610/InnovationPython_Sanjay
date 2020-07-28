# Write a program that accepts a hyphen-separated sequence of words as input and 
# prints the words in a hyphen-separated sequence after sorting them alphabetically.

sample = 'Run-through-the-jungle'

buffer_zone = sample.split("-")

buffer_zone.sort(key=str.casefold)
result=''

for word in buffer_zone:
    if word==buffer_zone[-1]:
        result = result+word
    else:
        result=result+word+"-"

print(result)