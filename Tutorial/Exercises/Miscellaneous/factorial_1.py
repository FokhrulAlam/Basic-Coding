number=int(input("Please enter a number to find factorial for: "))

prev_i=1

for i in range(1,number+1):
    i=prev_i*i
    prev_i=i

print(i)