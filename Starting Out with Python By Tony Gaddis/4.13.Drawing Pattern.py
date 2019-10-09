#Write a program that uses nested loops to draw this pattern:
#   *******
#   ******
#   *****
#   ****
#   ***
#   **
#   *

row=7
column=7

for i in range(row):
    for j in range(column):
        print("*",end='')
    column-=1
    print()