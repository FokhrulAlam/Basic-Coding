def update(x):
    print(id(x))
    x[1]='d'
    print(id(x))
    print(x)

a=['a','b','c']
print(a)
print(id(a))
update(a)
print(a)
print(id(a))
