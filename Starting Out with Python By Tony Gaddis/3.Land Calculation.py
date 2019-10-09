#One acre of land is equivalent to 43,560 square feet. Write a program that
#asks the user to enter the total square feet in a tract of land and
#calculates the number of acres in the tract.

Area=float(input("Please enter the total square feet in a tract "+\
                 "of land: "))
number_of_acres=Area/43560
print("The area in acres is ",format(number_of_acres,".2f"))