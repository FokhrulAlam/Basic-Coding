#I intentionally kept errors in this program. Please run it and fix it.

number=[]

for num in range(5):
    if num==0:
        print("Please enter five numbers:")

    number=[input()]

    if num==4:
        if number[0:5]%5==0:
                print(num)
                break #We want the first number only
        else:
            print("No number is divisible by 5.")