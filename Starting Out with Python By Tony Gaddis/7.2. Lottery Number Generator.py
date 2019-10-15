#Design a program that generates a seven-digit lottery number. The program should gener-ate seven random numbers,
# each in the range of 0 through 9, and assign each number to alist element.
# Then write another loop thatdisplays the contents of the list.

import random

def generate_random_numbers():
    digit_list=[]
    for digit in range(0,8):
        random_number=random.randint(0,9)
        digit_list.append(random_number)
    return digit_list

def display_lottery_number(lottery_number):
    print("The lottery number is: ",end='')
    for digit in lottery_number:
        print(digit,end='')

def main():
    random_number_list=generate_random_numbers()
    display_lottery_number(random_number_list)

main()