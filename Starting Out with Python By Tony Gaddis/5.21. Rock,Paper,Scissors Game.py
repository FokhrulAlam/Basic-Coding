#Write a program that lets the user play the game of Rock, Paper, Scissors against the com-puter. The program should
# work as follows.
        # 1.  When the program begins, a random number in the range of 1 through 3 is generated.If the number
# is 1, then the computer has chosen rock. If the number is 2, then the com-puter  has  chosen  paper.  If  the  number
# is  3,  then  the  computer  has  chosen  scissors.(Don’t display the computer’s choice yet.)
        # 2. The user enters his or her choice of “rock”, “paper”, or “scissors” at the keyboard.
        # 3.  The computer’s choice is displayed.
        # 4.  A winner is selected according to the following rules:•
# If  one  player  chooses  rock  and  the  other  player  chooses  scissors,  then  rock  wins.(The rock smashes the scissors.)•
# If one player chooses scissors and the other player chooses paper, then scissors wins.(Scissors cuts paper.)•
# If  one  player  chooses  paper  and  the  other  player  chooses  rock,  then  paper  wins.(Paper wraps rock.)•
# If both players make the same choice, the game must be played again to determine

import random

def generate_random_number():
    random_number=random.randint(1,3)
    return random_number

def computer_choice(random_number):
    if random_number==3:
        computer_choice='scissors'
    elif random_number==2:
        computer_choice='paper'
    else:
        computer_choice='rock'
    return computer_choice

def user_choice():
    return input("Please enter your choice: ")

def winner(computer_choice,user_choice):

    rock_message='The rock smashes the scissors'
    scissors_message="Scissors cuts paper"
    paper_message='Paper wraps rock'
    winner="No winner"
    message=''

    if computer_choice=='rock' and user_choice=='scissors':
        winner="Computer"
        message=rock_message
    elif computer_choice=='scissors' and user_choice=='rock':
        winner="User"
        message=rock_message
    elif computer_choice=='scissors' and user_choice=='paper':
        winner="Computer"
        message=scissors_message
    elif computer_choice=='paper' and user_choice=='scissors':
        winner="User"
        message=scissors_message
    elif computer_choice=='paper' and user_choice=='rock':
        winner="Computer"
        message=paper_message
    elif computer_choice=='rock' and user_choice=='paper':
        winner="User"
        message=paper_message

    return winner, message

def main():
    random_number=generate_random_number()
    comp_choice=computer_choice(random_number)
    users_choice=user_choice()

    print("The computer's choice is ", comp_choice)

    our_winner,message=winner(comp_choice,users_choice)

    if our_winner!="No winner":
        print("The winner is "+our_winner,message,sep='\n')
    while our_winner=="No winner":
        print("Warning: You both chose",comp_choice,'.',"Let's start Over.\n")
        our_winner=main()

main()