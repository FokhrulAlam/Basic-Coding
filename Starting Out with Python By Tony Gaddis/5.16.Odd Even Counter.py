#Write a program that generates 40 random numbers in between 1 and 1000, and keeps
# a count of how many of those random numbers are even and how many are odd.


import random

def random_number_generator():
    random_number=random.randint(1,1000)
    return random_number

def even_odd(number):
    if number%2==0:
        return True
    else:
        return False

def main():
    print("The numbers are:")
    even_number=0
    odd_number=0

    for i in range(40):
        random_number=random_number_generator()
        print(str(random_number)+' ',end='')
        if even_odd(random_number)==True:
            even_number+=1
        else:
            odd_number+=1
    print("\n\nTotal even numbers: "+str(even_number),"Total odd numbers: "+\
          str(odd_number),sep='\n')

main()