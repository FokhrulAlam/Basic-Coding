#Write a program to draw the following pattern:
#       ##
#       # #
#       #   #
#       #    #
#       #     #
#       #      #


for row in range(1,7):
    for column in range(row+1):
        if column==0 or column==row:
            print("#",end='')
        else:
            print(" ",end='')
    print()