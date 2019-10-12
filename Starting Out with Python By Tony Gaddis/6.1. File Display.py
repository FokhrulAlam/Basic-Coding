#Assume that a file containing a series of integers is named numbers.txt and exists on thecomputer’s disk. Write a
#program that displays all of the numbers in the file.

def main():
    # Assigning the memory address of numbers.txt to numbersFile
    numbersFile =open("numbers.txt", "r")

    line = numbersFile.readline()       #If it returns an empty string, we are at the end of the file

    while line != "":
        print(line.rstrip("\n"))
        line=numbersFile.readline()

main()
