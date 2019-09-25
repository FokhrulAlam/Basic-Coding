#Suppose we are passing a value of 200 to the function. The function will print the last fibonacci number less than 200


def fibonacci(n):
    first_number=0
    second_number=1

    previous_number=0
    current_number=1

    for i in range(n):
        next_number=current_number+previous_number
        if next_number>=n:
            print(current_number)
            break
        previous_number=current_number
        current_number=next_number

fibonacci(200)