#Write a code to print all the values from 1 to 100. skip the numbers divisible by 3 and 5.


i=1

while i<=100:
    if i%3!=0 and i%5!=0:
        print(i,'',end='')
    i=i+1
