def person(name,**kw):
    print(name)
    for i,j in kw.items():
        print(i,j)


person('navin',age=28,Address='Rajshahi',Mobile=2948993)