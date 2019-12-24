number=int(input("Please enter a number to find factorial for: "))

next_i=1

for i in range(number,0,-1):
    if i==1:
        print(i,'= ',end='')
    else:
        print(i,'x', end='')
    i=next_i*i
    next_i=i

print(i)