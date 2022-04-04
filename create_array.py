import numpy as np

# create array 
a = np.array(42)                                                #0 dimensional array
b = np.array([1, 2, 3, 4, 5])                                   #1 dimantional array
c = np.array([[1, 2, 3], [4, 5, 6]])                            #2 dimantional array 
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])  #3 dimantional array
e = np.array([1, 2, 3, 4], ndmin=6)                             #n dimantional array


print('------------------------------------------------')
print("Zero dimensional array")
print(a.ndim)   # print dimension of array    0
print(a)        # print array                 42  
print('------------------------------------------------')
print("One dimensional array") 
print(b.ndim)                           # 1
print(b)                                # [1 2 3 4 5]
print('------------------------------------------------')
print("Two dimensional array")
print(c.ndim)                           # 2
print(c)                         #       [[1 2 3]
                                 #        [4 5 6]]
print('------------------------------------------------')
print("Three dimensional array")
print(d.ndim)                           # 3
print(d)       
print('------------------------------------------------')
print("N dimensional array")
print(e.ndim)                           # N
print(e)      
print('-------------------------------------------------')



