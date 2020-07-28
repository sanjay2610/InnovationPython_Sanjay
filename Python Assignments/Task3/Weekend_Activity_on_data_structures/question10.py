"""
Write a program in Python to complete the following task:
 - Create two different lists as in even_list and odd_list
 - Ask the user to enter the number in the range of 1,50 and make sure if the entered number is even appended it to the even_list and if the entered number is odd append it to the odd list.
 - Keep that in mind you can only add 5 items in each list
 - Make sure once you entered the total 5 elements calculate the sum of the list and return the maximum out of the list.

"""

def cal_sum(list1):
    total=0
    for x in list1:
        total +=x

    print(list1)
    print("Sum of all the elements in the list", total)
    

even_list=[]
odd_list =[]

flag = True

while flag:
    if (len(even_list)==5 and len(odd_list)==5):
        print("Dead End")
        flag = False
        continue
    else:
        user_input = input("Enter a integer between 1 to 50: ")
        user_input = int(user_input)


        if (user_input%2==0):
            if len(even_list)<5:
                print("Number added in even list")
                even_list.append(user_input)
                if(len(even_list)==5):
                    cal_sum(even_list)
            continue
        else:   
            if len(odd_list)<=5:
                print("Number added in the odd list")
                odd_list.append(user_input)
                if len(odd_list)==5:
                    cal_sum(odd_list)
            continue
        
