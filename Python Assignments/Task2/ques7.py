#Write a program that prints all the numbers from 0 to 6 except 3 and 6

results = []

for n in range(7):
    if (n==3 or n==6):
        continue
    else:
        results.append(n)

print(results)