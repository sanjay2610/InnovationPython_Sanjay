count = 1
lucky_number = 7

while count<=5:
    number = input("Guess the lucky number: ")
    number = int(number)

    count+=1

    if number==lucky_number:
        print("Congratulations, you guessed the right number")
    elif(count==6):
        print("Game Over!")
    else:
        print("Try Again")
