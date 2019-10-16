#Write a program that gets a string containing a person’s first, middle, and last names, and then  display  their
# first, middle,  and  last  initials.  For  example,  if  the  user  enters  John William Smith the program should
# display J. W. S.

def name():
    first_name=input("Please enter your First name: ")
    middle_name=input("Please enter your middle name: ")
    last_name=input("Please enter your last name: ")
    return first_name,middle_name,last_name

def print_initials(first,middle,last):
    for i in first:
        print(i+". ",end='')
        break
    for i in middle:
        print(i+". ",end='')
        break
    for i in last:
        print(i+".")
        break

def main():
    first,middle,last=name()
    print_initials(first,middle,last)

main()