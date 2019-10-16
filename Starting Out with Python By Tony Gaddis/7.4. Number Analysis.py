#Design a program that asks the user to enter a series of 20 numbers. The program should store the numbers in a list
# and then display the following data:•
# The lowest number in the list•
# The highest number in the list•
# The total of the numbers in the list•
# The average of the numbers in the list


total_numbers=20

def lst_numbers():
    globals()
    list_of_numbers=[]
    print("Please enter 20 numbers below: ")
    for i in range(total_numbers):
        number=int(input())
        list_of_numbers.append(number)

    return list_of_numbers

def low_high(number_list):
    lowest_number=min(number_list)
    highest_number=max(number_list)
    return lowest_number, highest_number

def total_average(number_list):
    globals()
    total=0
    for number in number_list:
        total=total+number

    average=total/total_numbers
    return total,average

def print_values(low,high,total,average):
    print("\nThe lowest number is "+str(low),"The highest number is "+str(high),"The total of all numbers is "+str(total),\
          "The average is "+str(average),sep='\n')

def main():
    number_list=lst_numbers()
    low,high=low_high(number_list)
    total,average=total_average(number_list)
    print_values(low,high,total,average)

main()