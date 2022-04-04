import numpy as np

#How to create array ?
a = np.array(42)  #0 dimensional array
b = np.array([1, 2, 3, 4, 5]) #1 dimantional array
c = np.array([[1, 2, 3], [4, 5, 6]]) #2 dimantional array 
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) #3 dimantioal array
e = np.array([1, 2, 3, 4], ndmin=6) #n dimantional array

print('---------------------------------------')
print("Zero dimensional array")
print(a.ndim) 
print(a)        # print a array
print('---------------------------------------')
print("One dimensional array")
print(b.ndim)  
print(b)        # print b array
print('---------------------------------------')
print("Two dimensional array")
print(c.ndim)  
print(c)        # print c array
print('---------------------------------------')
print("Three dimensional array")
print(d.ndim)  
print(d)        # print d array
print('---------------------------------------')
print("N dimensional array")
print(e.ndim) 
print(e)        # print e array
print('---------------------------------------')



