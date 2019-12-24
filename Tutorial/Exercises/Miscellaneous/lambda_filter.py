even_func=lambda n:n%2==0

number=[1,2,4,4,5,3,6]
evens=list(filter(even_func,number))
print('Even= ',evens)

odd=list(filter(lambda n:n%2!=0,number))
print("Odd= ",odd)