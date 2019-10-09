#Write a program that lets the user enter a nonnegative integer and then uses a loop
#to calculate the factorial of that number. Display the factorial.

number=int(input("Please enter a non-negative whole number: "))
factorial=1

if number==0:
        print("The factorial of",number,"is 1")
elif number>0:
    for i in range(number,0,-1):
        factorial=i*factorial
    print("The factorial of",number,"is",factorial,'.')

while number<0:
    number=int(input("Please enter a non-negative whole number: "))
    if number<0:
        continue
    elif number==0:
        print("The factorial of",number,"is 1")
    else:
        for i in range(number,0,-1):
            factorial=i*factorial
        print("The factorial of",number,"is",factorial,'.')