#Assume that a file containing a series of names (as strings) is named names.txt and exists on the computer’s disk.
# Write a program that displays the number of names that are stored in the file. (Hint: Open the file and read every
# string stored in it. Use a variable to keep acount of the number of items that are read from the file.)

def main():
    #I just added some extensions using try, except, else
    try:
        opening_file=open("names.txt",'r')
    except Exception as error:
        print("There was a problem with the file: ",error)
    else:
        names=opening_file.readline()
        number_of_names=0

        while names != "":
            number_of_names+=1
            names=opening_file.readline()

        opening_file.close()
        print("There are",number_of_names,"names in the file.")

main()