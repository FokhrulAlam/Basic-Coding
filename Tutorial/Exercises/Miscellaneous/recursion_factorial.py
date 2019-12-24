def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)


factorial=fact(int(input("Please enter a whole number: ")))
print(factorial)