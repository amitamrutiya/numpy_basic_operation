import numpy as np

arr1 = np.array([8, 7, 6, 5])            # create first array
arr2 = np.array([4, 3, 2, 1])            # create second array

print('-----------------------------------------------------')
print("Addition of an array :")
newarr = np.add(arr1, arr2)
print(newarr)                             # [12 10 8 6]
print("Subraction of an array :")
newarr = np.subtract(arr1, arr2)
print(newarr)                             # [4 4 4 4]
print("Multiplication of an array :")
newarr = np.multiply(arr1, arr2)
print(newarr)                             # [32 21 12 5]
print("Division of an array :")
newarr = np.divide(arr1, arr2)
print(newarr)                             # [2.00 2.33 3.00 5.00 ]
print("Power of an array :")
newarr = np.power(arr1, arr2)
print(newarr)                             # [4096 343 36 5]
print("Modulation of an array :")
newarr = np.mod(arr1, arr2)
print(newarr)                             # [0 1 0 0]

print('-----------------------------------------------------')
print("Floor Value :")
arr = np.floor([-3.1666, 3.6667])         # minimum value
print(arr)                                # [-4.  3.]
print("Ceil Value :")
arr = np.ceil([-3.1666, 3.6667])          # maximum value
print(arr)                                # [-3.  4.]

print('-----------------------------------------------------')
arr = np.arange(5, 8)
print("Log of the number :")
print(np.log2(arr))                       # [2.3219 2.5848  2.8072]

print('-----------------------------------------------------')
print("Sum of a same array :")
newarr = np.cumsum(arr)
print(newarr)                             # [5 11 18]
print("Product of a same array :")
newarr = np.cumprod(arr)
print(newarr)                             # [5 30 210]
print("Difference of same array :")
newarr = np.diff(arr)
print(newarr)                             # [1 1]

print('------------------------------------------------------')
num1 = 4
num2 = 6

print("LCM of two value :" )
x = np.lcm(num1, num2)    # find a lcm of two value
print(x)                                    # 12

print("GCD of two value :")
x = np.gcd(num1, num2)    # find a gcm of two value
print(x)                                    # 2  
