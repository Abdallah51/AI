import numpy as np

#define array
my_array=np.array([10,20,30,40])
print(my_array)

print(type(my_array))
print(my_array.shape)

#Access My array
print(my_array[1])
my_array[1]=55
print(my_array)

print(my_array[0:2])

#Multidimensional array
my_array_2=np.array([[10,20,30,40],[50,60,70,80]])
print(my_array_2)

print(type(my_array_2))
print(my_array_2.shape)

"""indexing & slicing"""

print(my_array_2[0][0])
print(my_array_2[1][0])

print(my_array_2[1:2])

"""Cratinh Automatic array

```
Type Of Arrays
1-Zero
2-Ones
3-Constant
4-Identity
5-Random
```
"""

#ZERO Matrix
zero_array = np.zeros((3,3))
print(zero_array)

#ONES MATRIX
one_array = np.ones((3,3))
print(one_array)

#CONSTANT TYPE ARRAY
constant_type = np.full((3,3),7)
print(constant_type)

#IDENTITY MATRIX
ident = np.eye(3)
print(ident)

#RANDOM MATRIX
random_matrix = np.random.random((3,3))
print(random_matrix)

#Numerical Data Types
x_int = np.array(([1,2],[3,4]))
print(x_int.dtype)

y_float = np.random.random((3,3))
print(y_float.dtype)

#Arithmatic Operations
x_array=np.array([[1,2,3],[4,5,6]])
y_array=np.array([[10,20,30],[40,50,60]])
print(x_array.shape)
print(x_array.shape)

#Add
print(np.add(x_array,y_array))

#Sub
print(np.subtract(x_array,y_array))

#Mul
print(np.multiply(x_array,y_array))

#Div
print(np.divide(y_array,x_array))

#sprt
print(np.sqrt(x_array))

x_new = np.sqrt(x_array)
y_new = np.divide(x_array,y_array)
z_new = np.multiply(x_new,y_new)
print(z_new)

#Dot Produc
x_dot_array=np.array([[1,2],[3,4]])
y_dot_array=np.array([[5,6],[7,8]])

v_dot_array=np.array([9,10])
w_dot_array=np.array([11,12])

print(x_dot_array.dot(v_dot_array))
print(v_dot_array.dot(x_dot_array))
print(x_dot_array.dot(y_dot_array))

#Transpose
x_transpose_array=np.array([[1,2],[3,4]])
print("original",x_transpose_array)
print("transpose",x_transpose_array.T)

#Broadcasting
v_broadcasting = np.array([1,0,1])
vv=np.tile(v_broadcasting,(4,1))
print(vv)

