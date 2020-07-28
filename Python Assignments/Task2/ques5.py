def div5(num):
    if num%5==0:
        return True
    else:
         return False

def div7(num):
    if num%7==0:
        return True
    else:
         return False


results = []

for number in range(2000, 3200):
    if div7(number) and not div5(number):
        results.append(number)

print(results)


