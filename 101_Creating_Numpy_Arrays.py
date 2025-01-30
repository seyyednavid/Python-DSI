

import numpy as np


my_1d_array = np.array([1, 2, 3])
type(my_1d_array)

my_1d_array.shape #(3,)
my_1d_array.ndim  # 1

my_1d_array[0]

my_1d_array[0:2]

my_1d_array[-1]


my_2d_array = np.array([[1, 2, 3 , 4, 5],[6, 7, 8, 9, 10]])
print(my_2d_array)

my_2d_array.shape  # (2, 5)
my_2d_array.ndim   # 2


my_2d_array[0]  # array([1, 2, 3, 4, 5])
my_2d_array[1]  # array([ 6,  7,  8,  9, 10])


my_2d_array[0][1] # 2
my_2d_array[0,1]  # 2


my_2d_array[0:2,1:3]  




np.zeros(3)
np.zeros((3,3))
np.zeros((3,3,3))


np.ones(3)
np.ones((3,3))
np.ones((3,3,3))


np.full((3,3), 5)



np.arange(10)     # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.arange(2,10)   # array([2, 3, 4, 5, 6, 7, 8, 9])
np.arange(2,10,2) # array([2, 4, 6, 8])



np.linspace(1, 5, 20)


float_array = np.linspace(1, 5, 20)
np.round(float_array, 2)


np.random.rand(5)
np.random.rand(5,2)


np.random.randint(20,80,100)
np.random.randint(20,80,(10,10))

my_1d_array = np.random.randint(20, 80, 100)
print(my_1d_array)

my_2d_array = my_1d_array.reshape(10,10)
print(my_2d_array)
















































