a=10
print('id of a ',id(a))

def something():
    a=4

    x=globals()['a']
    print('id of x',id(x))
    print('value of x ',x)

    globals()['a']=15

    print('id of x', id(x))
    print('value of x ',x)

something()
print('value of a ',a)
print('id of a ',id(a))