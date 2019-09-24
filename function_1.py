def update(x):
    print(id(x))
    x=5
    print(id(x))
    print(x)

a=1
print(a)
print(id(a))
update(a)
print(a)
print(id(a))