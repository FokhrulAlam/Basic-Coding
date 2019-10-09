#Write a program that asks the user for a number in the range of 1 through 7.
#The program should display the corresponding day of the week.
#where 1=Monday,2=Tuesday.........7=Sunday. The program should display
#an error message if the user enters a number that is outside the range of 1 through 7.

number=int(input("Please enter a number to know the day: "))

if number==1:
    print("It's monday.")
elif number==2:
    print("It's tuesday.")
elif number==3:
    print("It's wednesday.")
elif number==4:
    print("It's thursday.")
elif number==5:
    print("It's friday.")
elif number==6:
    print("It's saturday.")
elif number==7:
    print("It's sunday.")
else:
    print("Error: The number should be between 1 and 7,inclusive")