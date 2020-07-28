#Write a program to get the sum and multiply of all the items in a given list.

list1= [1,4,7,2]

sum_total = 0
mul = 1

for num in list1:
    sum_total +=num
    mul *=num

print("Sum Total of all elements: ", sum_total)
print("Product of all the elements in the list", mul)

print("Largest number in the list: ", max(list1))
print("Smallest number in the list: ", min(list1))