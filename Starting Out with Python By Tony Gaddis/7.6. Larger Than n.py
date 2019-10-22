#In a program, write a function that accepts two arguments: a list, and a number n. Assume that the list
# contains numbers. the function should display all of the numbers in the list that are greater than the number n.


def list_numbers():
    total_numbers=int(input("How many numbers you want to insert: "))
    list_of_numbers=[]
    for i in range(total_numbers):
        number=int(input())
        list_of_numbers.append(number)
    return list_of_numbers

def greater_than_n(list,single_number):
    for numbers in list:
        if numbers>single_number:
            print(str(numbers)+" ",end='')
def main():
    single_number = int(input("Please insert a number to compare with the numbers in the list: "))
    number_list=list_numbers()
    greater_than_n(number_list,single_number)

main()