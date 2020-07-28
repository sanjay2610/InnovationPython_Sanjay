#Write a program to replace the last element in a list with another list.

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]

list1[-1:] = list2

print(list1)