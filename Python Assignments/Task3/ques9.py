#Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).

n = 5

result={}

for x in range(1,n+1):
    result[x] = x**2

print(result)

