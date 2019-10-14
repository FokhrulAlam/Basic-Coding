#This exercise assumes you have completed Programming Exercise 7, Random Number File Writer.  Write  another  program
# that  reads  the  random  numbers  from  the  file,  display  the numbers, and then display the following data:•
# The total of the numbers•
# The number of random numbers read from the file

def display_numbers(file_tobe_read):
    try:
        random_number_file=open(file_tobe_read,'r')
    except Exception as error:
        print("Warning: Problem with opening the file mentioned: ",error)
    else:
        lines=random_number_file.readline()
        number_of_random_numbers=0
        total_of_numbers=0

        print("The random numbers are: ")
        while lines != "":
            new_line= lines.strip()          #Stripping the line \n character
            for numbers in map(int,new_line.split()):           #separating the integers
                print(numbers)
                number_of_random_numbers+=1
                total_of_numbers=total_of_numbers+numbers
            lines=random_number_file.readline()

        print("\nThe total of the numbers is ",total_of_numbers)
        print("There are total",number_of_random_numbers,"random numbers in the file")
    finally:
        print("\nCongratulations! You successfully read the numbers.")
def main():
    display_numbers("RandomNumbers.txt")

main()