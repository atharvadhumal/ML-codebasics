import numpy as np

# arr = np.array([1, 2, 3])
# print(arr)

# l = [1, 2, 3]
# print(l)

# # the numpy array looks same as the lists in python but it occupies less memory as compared to python lists

# python_list = list(range(100))
# print(python_list[:5])

# import sys

# print(sys.getsizeof(python_list[0])*len(python_list))
# #takes 2400

# numpy_array = np.array(100)
# numpy_array[:5]

# print(numpy_array.nbytes)
# #whereas this takes 400 only

import time

SIZE = 1000000

l1 = list(range(SIZE))
l2 = list(range(SIZE))

start_time = time.time()
l3 = [x+y for x, y in zip(l1, l2)]
end_time = time.time()

print("Python list took ", end_time-start_time)

n1 = np.arange(SIZE)
n2 = np.arange(SIZE)

start_time = time.time()
n3 = n1 + n2
end_time = time.time()

print("Numpy array took ", end_time-start_time)