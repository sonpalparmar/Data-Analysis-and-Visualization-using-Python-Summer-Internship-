'''
Lottery program
1. It gives user 20 choices to choose from
2. If user choses the right one he wins the prize  
3. It also shows the winners
'''

import random

def main():
    lottery_numbers = []
    while len(lottery_numbers) < 20:
        n = random.randint(100, 999)
        if n not in lottery_numbers:
            lottery_numbers.append(n)

    print("Index \t  number")
    for i in range(len(lottery_numbers)):
        print(format(i+1, "3d"), " \t ", format(lottery_numbers[i], "5d"))

    winners = []
    while len(winners) < 3:
        n = random.choice(lottery_numbers)
        if n not in winners:
            winners.append(n)

    number = eval(input("Enter the index of lottery : "))

    if (number > 20 or number < 0):
        print("Inavlid index")
        return

    if (lottery_numbers[number] == winners[0]):
        print("Congratulations! You won the 1st prize of Rs 10,000 in lottery!")
    elif (lottery_numbers[number] == winners[1]):
        print("Congratulations! You won the 2nd prize of Rs 5,000 in lottery!")
    elif (lottery_numbers[number] == winners[2]):
        print("Congratulations! You won the 3rd prize of Rs 100 in lottery!")
    else:
        print("Sorry you couldn't win, Try again !!!")

    print("These were the winners : ")
    for i in winners:
        print(format(i, "4d"))


main()
