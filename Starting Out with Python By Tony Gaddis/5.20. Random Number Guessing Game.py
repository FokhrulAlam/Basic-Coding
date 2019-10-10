#Write a program that generates a random number in the range of 1 through 100 and asks theuser to guess what the number
#is. If the user’s guess is higher than the random number, the pro-gram should display “Too high, try again.” If the
# user’s guess is lower than the random num-ber, the program should display “Too low, try again.” If the user guesses
# the number, the appli-cation should congratulate the user and then generate a new random number so the game canstart
# over.
# Optional Enhancement: Enhance the game so it keeps count of the number of guesses that theuser makes. When the user
# correctly guesses the random number, the program should displaythe number of guesses.

import random

number_of_guesses=0
number_of_correct_guesses=0

def generate_random_number():
    return random.randint(1,100)

def user_guess():
    user=int(input("Please choose a number in between 1 and 100: "))

    while user<1 or user>100:
        print("Your chosen number is out of range.")
        user = int(input("Please choose a number in between 1 and 100: "))

        if user>=1 and user<=100:
            return user
            break
        else:
            continue
    else:
        return user

def number_comparison():
    global number_of_guesses
    global number_of_correct_guesses

    user=user_guess()
    random_number=generate_random_number()

    if user>random_number:
        print("Too high, try again.")
        number_of_guesses+=1

        if number_of_guesses<=970:
            number_comparison()
        else:
            print("\nThat's all today. Thanks.")
            print("Total number of guesses you made: ", number_of_guesses)
            print("Total number of correct guesses: ", number_of_correct_guesses)

    elif user<random_number:
        print("Too low, try again.")
        number_of_guesses+=1

        if number_of_guesses<=970:
            number_comparison()
        else:
            print("\nThat's all today. Thanks.")
            print("Total number of guesses you made: ", number_of_guesses)
            print("Total number of correct guesses: ", number_of_correct_guesses)

    elif user==random_number:
        number_of_correct_guesses=number_of_correct_guesses+1
        number_of_guesses=number_of_guesses+1

        if number_of_guesses <= 970:
            print("\nCongratulation! You are right. You are encouraged to try more.")
            print("Total number of guesses you made: ", number_of_guesses)
            print("Total number of correct guesses: ", number_of_correct_guesses, '\n')
            number_comparison()
        else:
            print("\nCongratulation! You are right.")
            print("Total number of guesses you made: ", number_of_guesses)
            print("Total number of correct guesses: ", number_of_correct_guesses)
            print("That's all today. Thanks.")

def main():
    number_comparison()

main()