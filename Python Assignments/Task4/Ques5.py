"""
 Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Sample input:
Hello world
Practice makes perfect
Expected Output:
HELLO WORLD
PRACTICE MAKES PERFECT
"""
lines = []
while True:
    line = input("Enter a line: ")
    if line:
        lines.append(line.upper())
    else:
        break;

for line in lines:
    print(line)