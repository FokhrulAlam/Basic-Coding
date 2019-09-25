def fibonacci(n):
    first_number=0
    second_number=1

    previous_number=0
    current_number=1

    if n==1:
        print(first_number,end='')

    else:
        print(first_number,second_number,end='')
        for i in range(n-2):
            next_number=current_number+previous_number
            print('',next_number,end='')
            previous_number=current_number
            current_number=next_number

fibonacci(12)