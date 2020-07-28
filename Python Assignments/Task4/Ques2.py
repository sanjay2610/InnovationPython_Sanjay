"""
Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
Expected Output:
No. of Upper case characters : 3
No. of Lower case Characters : 12
"""

upper, lower = 0,0
sample = 'Sweet Child of Mine'

for n in sample:
    if n.islower():
        lower+=1
    elif n.isupper():
        upper+=1

print("Number of lowercase letter: ", lower)
print("Number of uppercase letter: ", upper)