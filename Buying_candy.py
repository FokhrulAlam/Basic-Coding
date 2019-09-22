x=int(input("How many candies do you want? "))
if x>20 or x<=0:
    Attention=(str(input("Hey, we have only 20 candies.\nDo you want them?\nSay yes or no: ")))
    if Attention=='yes':
        y=int(input("Tell a whole number in between 1 and 20, inclusive: "))
        while y>20 or y<=0:
            Warning=(int(input('Please tell a whole number in between 1 and 20, inclusive: ')))
            if Warning>20 or Warning<=0:
                continue
            elif Warning<=20 and Warning>0:
                print('OK. Thanks. I am printing them below.')
                i = 1
                while i <= Warning:
                    print("Candy")
                    i += 1
            if i>Warning:
                break
    if Attention=='no':
        print("Ok. Thanks. See you.")
if x<=20 and x>0:
    print('Ok.Thanks.I am printing them below.')
    i=1
    while i<=x:
        print("Candy")
        i+=1