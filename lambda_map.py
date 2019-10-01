num=[1,2,4,6,3,7,10]

odd=list(filter(lambda n: n%2!=0,num))

double_odd=list(map(lambda a: a*2,odd))

print(double_odd)
