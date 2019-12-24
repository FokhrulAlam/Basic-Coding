from numpy import *

arr1=array([
    [2,6,4,6],
    [1,7,0,2]
])
#Knowing data type
print("Data type ",arr1.dtype)
print("Dimension ",arr1.ndim)
print("Shape ",arr1.shape)
print("Size ",arr1.size)
#Converting arr1 into 1-D array
arr2=arr1.flatten()
print("One dimensional arr2 ",arr2)
#Creating 2-D array of 2 rows and 3 columns from the 1-D array
arr3=arr2.reshape(2,4)
print("2-D array arr3")
print(arr3)
#Creating a 3-D array having two 2-D arrays each with two columns
arr4=arr3.reshape(2,2,2)
print("3-D array arr4 ")
print(arr4)