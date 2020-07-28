#Create a new list that contains the specified numbers after removing the even numbers from a predefined list.

list1 = [1,2,3,4,5,6,7,8,9]

for n in list1:
    if n%2==0:
        list1.remove(n)

print(list1)