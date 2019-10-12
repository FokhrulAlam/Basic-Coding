#Write a program that asks the user for the name of a file. The program should display the contents of the file with
# each line preceded with a line number followed by a colon. The line numbering should start at 1.

def main():
    file_name=input("Please enter the file name: ")
    print()

    file_opening=open(file_name,'r')
    lines=file_opening.readline()
    line_number=1

    while lines != "":
        print(str(line_number)+':',lines.strip('\n'))

        line_number+=1
        lines=file_opening.readline()

    file_opening.close()

main()