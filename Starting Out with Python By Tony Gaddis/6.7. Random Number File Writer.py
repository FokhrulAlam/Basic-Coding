#Write  a  program  that  writes  a  series  of  random  numbers  to  a  file.  Each  random  number should be in the
# range of 1 through 500. The application should let the user specify how many random numbers the file will hold.

import random

def generate_random_number():
    random_number=random.randint(1,500)
    return random_number

def main():
    total_numbers=int(input("How many random numbers the file will hold? Ans: "))
    try:
        file_to_write_to = open("RandomNumbers.txt", 'w')
    except Exception as error:
        print("Error with the file: ",error)

    else:
        new_line_after_numbers=20
        for i in range(1,total_numbers+1):
            random_number=generate_random_number()
            if i==new_line_after_numbers+1:
                file_to_write_to.write("\n"+str(random_number)+' ')
                new_line_after_numbers+=20
            else:
                file_to_write_to.write(str(random_number)+' ')

        print(i,"numbers have been written to the file RandomNumbers.txt")

    finally:
        file_to_write_to.close()
        print("End of program")

main()