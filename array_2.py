from array import *
arr=array('i',[])
n=int(input("Enter the length of the array:"))
for i in range(n):
    x=int(input("Enter the value:"))
    arr.append(x)
print(arr)

value=int(input("Enter a value to know its index: "))
for i in arr:
    if value==arr[i]:
        index=[i]
        print("Index of value is ",index)
        break