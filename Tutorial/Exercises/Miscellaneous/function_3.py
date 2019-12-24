def sum(a,*b):
    c=a

    for i in range(len(b)):
        c=c+b[i]
    print(c)

sum(2,3,4,6,7)