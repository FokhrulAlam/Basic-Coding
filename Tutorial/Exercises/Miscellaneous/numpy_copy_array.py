from numpy import *
arr1=array([2,4,6,7,8])

arr2=arr1.view()
arr1[1]=5
print("View arr1 ",arr1)
print("View arr2 ",arr2)

arr3=array([8,3,0,2,5])

arr4=arr3.copy()
arr3[1]=5
print("View arr3 ",arr3)
print("View arr4 ",arr4)

arr5=arr4
arr4[4]=3
print("arr4 ",arr4)
print("arr5 ",arr5)
