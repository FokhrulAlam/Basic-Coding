def Hey():
    print("Hello World")

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

Hey()

result1,result2=add_sub(7,7)
print(result1,result2)