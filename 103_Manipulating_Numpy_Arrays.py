

import numpy as np


my_1d_array = np.zeros(10)
print(my_1d_array)

my_1d_array[0] = 50
print(my_1d_array)


my_1d_array[3:6] = 50
print(my_1d_array)


np.where(my_1d_array == 50)


my_2d_array = np.array([[1,5,9],[8,5,5]])
print(my_2d_array)


np.where(my_2d_array == 5) 
np.where(my_2d_array < 5) 
np.where(my_2d_array >= 5) 
np.where(my_2d_array != 5) 
# (array([0, 0, 1], dtype=int64), array([0, 2, 0], dtype=int64))


np.argwhere(my_2d_array == 5) 
""" array([[0, 1],
       [1, 1],
       [1, 2]], dtype=int64) """



index = np.where(my_2d_array > 5)
print(index) # (array([0, 1], dtype=int64), array([2, 0], dtype=int64))

my_2d_array[index] #array([9, 8])

my_2d_array[index] = 100



np.all(my_1d_array)      # False => means all values are non zero
np.all(my_1d_array >= 0) # True
np.all(my_1d_array > 5)


np.any(my_1d_array) #  True



a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(a)
print(b)

v = np.vstack((a,b))
print(v)

np.vstack((a,b,a,b))



h = np.hstack((a,b))
print(h)

np.hstack((a,b,a,b))



print(my_2d_array)
my_2d_array.flatten()


























