import numpy as np
'''
    NumPy is a Python library that provides multidimensional arrays (2D, 3D, ..., nD), an assortment of routines for fast operations (logical, mathmatical, etc.), and much more.

    The ndarray object is the core of NumPy. It is the n-dimensional arrays of homogeneous (the same) data types. Some differences between NumPy arrays and standard Python are:
        - NumPy arrays have a fixed size at creation, unlike Python lists which grow dynamically. So when changing the size of a NumPy array it creates a new one and deletes the original.
        - NumPy arrays require every element to be the same data type (homogeneous). There is an exeception but for now don't worry about it.
        - NumPy is faster than normal Python operations in the context of large numbers of data. So Python's built-in sequences are more efficient and less code for smaller operations.

    Why is NumPy fast? 
        - Vectorization or the absence of looping, indexing, etc. in the code and rather having it pre-compiled.

'''


# .arange | creating a numpy array of index range 20, so 0-19. It is then .reshaped | which is the dimensions of the array.
a = np.arange(20).reshape(4,5) # this is an ndarray 
print(f"a = {a}")

# .shape | returns dimensions of array. This will come as a tuple, not a count, and give the length, width, depth, etc. of a numpy array.
print(a.shape)

# .ndim | returns the number/count of axes/dimensions in the array.
print(a.ndim)

# .size | returns total number of elements in the array.
print(a.size)

# .dtype | returns the type of the elements in the array.
print(a.dtype)

# .itemsize | returns the size, in bytes, of each element of the array.
print(a.itemsize)

# Different ways to create an array
a = np.array([2, 3, 4]) # 1D int array
print(f"a = {a}")
b = np.array([2.1, 3.2, 4.7]) # 1D float array
print(f"b = {b}")
a = np.array([(1, 2, 3), (4, 5, 6)])
print(f"a = {a}") # 2D int array
c = np.array([(1, 2, 3), (3, 4, 1)], dtype=complex)
print(f"c = {c}") # returns 2D complex array

# .zeros, .ones, .empty | creates an array full of value 0, 1, or random content based on memory state. can use dtype= to specify for .empty initialization.
d = np.zeros((3, 4))
print(f"d = {d}")
d = np.ones((2, 3, 4), dtype=np.int16)
print(f"d = {d}")
d = np.empty((2, 3)) # will default to float since no dtype specified
print(f"d = {d}")