from array import *
arr=array('i',[])
arr_1=array('i',[])
print("Please enter five numbers:\n")
for i in range(5):
    number=int(input())
    arr.append(number)
print(arr)
for j in arr:
    if j!=arr[2]:
        arr_1.append(j)
print(arr_1)