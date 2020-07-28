flag = True
lucky_number = 7

while flag:
    number = input("Guess the lucky number: ")
    number = int(number)
    if number==lucky_number:
        flag=False
        print("Congratulations, you guessed the right number")
    else:
        answer = input("Do you want to give it a another try? (y/n) ")
        if (answer.lower() =='y'):
            continue
        else:
            flag=False


