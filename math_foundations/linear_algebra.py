
import math
from typing import List, Optional

# Write a Python function from scratch — no NumPy — that takes two vectors as lists and returns their cosine similarity.

dataSetI = [3, 45, 7, 2]
dataSetII = [2, 54, 13, 15]
dataSetIII = [1, 2, 3]

def dot_product(a: List[int], b: List[int]) -> int:

    if len(a) != len(b):
        raise ValueError("Vectors must be the same length")
    return sum(x * y for x,y in zip(a, b))

def magnitude(a: List[int]):
    return math.sqrt(dot_product(a, a))

def consine_similarity(a: List[int], b: List[int]) -> float:
    # compute cosine similarity of a to b: (a dot b)/{||a||*||b||)
    return dot_product(a, b) / (magnitude(a) * magnitude(b) )

print(consine_similarity(dataSetI, dataSetII))
print(consine_similarity(dataSetIII, dataSetIII))

# Write a matrix-vector multiplication from scratch — no NumPy:
def mat_vec_multiply(matrix: List[List[float]], vector: List[float]) -> List[float]:
    # matrix is a list of rows
    # each row dotted with the vector gives one output element
    # Multiplies a matrix by a vector from scratch, returning the resulting vector.
    # The number of columns in the matrix must equal the length of the vector.
    # Get the number of rows (M) and columns (N) from the matrix shape
    if len(matrix) == 0:
        return []
    if len(matrix[0]) != len(vector):
        raise ValueError(f"Matrix columns ({len(matrix[0])}) must match vector length ({len(vector)})")
    
    return [dot_product(row, vector) for row in matrix]
           
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]
vector1 = [1, 0, 1]

print(mat_vec_multiply(matrix1, vector1))

# Given a dataset of vectors and one principal component vector, project every data point onto that component.
def project_data(data: List[List[float]], principal_component: List[float]) -> List[float]:
    # project each data point onto the principal component
    # hint: projection of a point onto a direction = dot_product(point, principal_component)
    # return a list of scalar values — one per data point
    return [dot_product(row, principal_component) for row in data]
    
data1 = [
    [5, 1, 4],  # User 1
    [4, 1, 5],  # User 2
    [2, 5, 2],  # User 3
    [1, 5, 1],  # User 4
    [3, 3, 3],  # User 5
]

principal_component1 = [1, -1, 1]  # rough "action vs romance" direction

print(project_data(data1, principal_component1))
