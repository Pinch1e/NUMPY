#The ndim attribute of a NumPy array is used to determine the number of dimensions (axes) of the array.Prints an integer value representing the number of dimensions.

import numpy as np 

a = np.array(45)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3], [4,5,6]])
d = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])

#print(a.ndim)
#print(b.ndim)
#print(c.ndim)
#print(d.ndim)

#print(a)
#print(b)
#print(c)
#print(d)

arr = np.array([1,2,3,4,5], ndmin = 5)
print(arr)
print("Number of Dimension : ", arr.ndim)

