from array import *
arr=array('i',[])
rev_arr=array('i',[])
n=int(input("How many numbers do you want to put? "))
print("Please enter the numbers of the array:")
for i in range(n):
    number=int(input())
    arr.append(number)
print("The original array is ",arr)
for j in range(n-1,-1,-1):
    rev_arr.append(arr[j])
print("The reverse array is ",rev_arr)