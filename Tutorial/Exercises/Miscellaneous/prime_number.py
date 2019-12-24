number=int(input("Please enter a whole number greater than one:"))

while number<=1:
    num = int(input("Please enter a whole number greater than one:"))
    if num>1:
        for i in range(2, num):
            if num % i == 0:
                print("It's not a prime number.")
                break
            else:
                print("It's a prime number.")
        break
    else:
        continue
while number>2:
    for i in range(2,number):
        if number%i==0:
            print("It's not a prime number.")
            break
        else:
            print("It's a prime number.")
    break
while number==2:
    print("It is a prime number.")
    break

