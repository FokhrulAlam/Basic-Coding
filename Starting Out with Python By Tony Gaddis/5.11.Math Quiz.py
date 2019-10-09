#Write a program that gives simple math quizzes. The program should display two random
#numbers that are to be added, such as:
#   6
#  +11
#The program should allow the student to enter the answer.If the answer is correct, a message
#of congratulations should be displayed. If the answer is incorrect, a messge showing the correct
#answer should be displayed.

import random

def random_number():
    random_number1=random.randint(1,250)
    random_number2=random.randint(1,250)
    return random_number1,random_number2

def Question():
    num1,num2=random_number()
    sum_by_user=int(input("What is the sum of "+str(num1)+" and "+str(num2)+" ? Ans: "))
    return sum_by_user==num1+num2
def main():
    if Question()==True:
        print("Congratulations!!!\n\tYour answer is correct! Keep going!")
    else:
        print("Sorry,your answer is wrong!")


main()