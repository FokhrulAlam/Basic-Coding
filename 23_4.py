for i in range(4):
    tup_1=('A','B','C','D')
    tup_2=('P','Q','R')
    for j in range(i+1):
        print(tup_1[j],'',end='')
    for k in range(3-i):
        print(tup_2[k+i],'',end='')
    print()