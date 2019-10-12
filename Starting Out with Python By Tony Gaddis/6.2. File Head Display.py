#Write a program that asks the user for the name of a file. The program should display onlythe first five lines of the
# file’s contents. If the file contains less than five lines, it should dis-play the file’s entire contents.

def main():
    file_name=input("Please enter the name of the file: ")
    print()
    
    file_opening=open(file_name,'r')
    lines = file_opening.readline()
    line_number=1

    while lines != "" and line_number<=5:
        print(lines.rstrip('\n'))
        line_number+=1
        lines=file_opening.readline()

    file_opening.close()

main()

