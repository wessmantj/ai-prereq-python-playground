# NUMPY OVERVIEW
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


# .arange | here is creating a numpy array of index range 20, so 0-19. Is the same as python function range, but returns an array. It is then .reshaped | which is the dimensions of the array.
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

# printing a NumPy array that is larger than printable, it will skip the central part and only return the corners. Can be changed with .setprintoptions | either sys.maxsize or desired output.

# COSINE SIMILARITY

from numpy.linalg import norm

# Computing the consine similarity between two 1D vectors
a = np.array([2, 1, 2, 3, 2, 9])
b = np.array([3, 4, 2, 4, 5, 5])
# .dot | computes the dot product or each index of a times each index of b. An example can be np.dot([1, 2, 3], [4, 5, 6]), which results in (1*4) + (2*5) + (3*6) = 32
# .norm | computes the magnitude of an array 
cosine = np.dot(a, b) / (norm(a) * norm(b)) # (a * b) / (||a|| * ||b||)
print(f"Cosine Similarity: {cosine}")

# Computing similarity between vector and batch of vectors
a = np.array([[2, 1, 2], [3, 2, 9], [-1, 2, -3]]) # has 3 vectors (rows)
b = np.array([3, 4, 2])

cosine = np.dot(a, b) / (norm(a, axis=1) * norm(b)) # similarity is computed row-wise
print("Cosine Similarity:", cosine)

# Similarity between two martrices
a = np.array([[1, 2, 2], [3, 2, 2], [-2, 1, -3]])
b = np.array([[4, 2, 4], [2, -2, 5], [3, 4, -4]])

cosine = np.sum(a * b, axis=1) / (norm(a, axis=1) * norm(b, axis=1))
print(f"Cosine Similarity: {cosine}")

"""
Final Explaination:
    Why is this useful for embeddings?
    
    An embedding is simply a vector representation of some object (text, image, user, etc.), which in Python is typically stored as a NumPy ndarry. NumPy in Python is a library for manipulating arrays and performing fast numerical operations, most importantly for this case linear algrebra on n-dimensional arrasy such as matrices and vectors. With embeddings this works well since calculating dot products, norms, and other operations need to be done at scale, which regular Python wouldn't be ideal. 

    Now, say I am given a collection of embeddings, the question is how do I measure similarity between them so I can use semantic search and retrieval-augemented generation or RAG. With an embedding model, it has already learned a high-dimensional space where semantically similar items are mapped to nearby directions. Our job is to compare these vectors in that space. A common metric for this is consine similarity, which is a formula to measure the consine and angle between teo vectors (a and b). If the angle is 0, meaning they point in the same direction, then cos(0) = 1, indicating maximum similarity. While if the angle is 90, then cos(pi/2) = 0, or that they are unrelated. 

    So in semantic search the typical workflow is: turn the user query into an embedding -> compute the cosine similarity between that query and all stored document vectors, then retrieve the top-k documents with the highest cosine scores. Thus, embedding provides a geometric representation of meaning, NumPy provides the tools to manipulate these vectors in Python, and cosine similarity provides a scoring rule that tells us which stored embeddings are relevant.
"""