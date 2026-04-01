import faiss
import numpy as np
from IPython.display import display
import time
'''
What is FAISS?
    Faiss (Facebook AI Similarity Search) is an open source library developed my Meta to efficently similarity search and cluster dense vectors. These dense vectors its desinged to handle range from a few million to over a billion high-dimensional vectors, making it the backbone for modern reccomendation systems, search engines and AI applications.

    Important Notes:
     - the library itself provides highly optimized algorithms and data structures for nearest neighbor search and clustering.
     - it uses both the CPUs and GPUs for max performance.
'''


'''
    INDEXFLATL2 is the main brute-force indexing approach in fiass. What it does is store all vectors in memory and performs a brute-force search to find the nearest neighbors using Eucliden distance ( or the straightest and shortest path between two points ).
     - best for small -> medium datasets
     - where exeact result is required
     - when returning the exact nearest neighbor
     - simple to impliment and use, yet not scaleable

'''



d = 128 # the number of features per vector / dimension
nb = 100000 # the number of vectors within the database
nq = 10 # the number of query vectors you want to search

# both are random float nparrays simulating the database and queries
xb = np.random.random((nb, d)).astype('float32')
xq = np.random.random((nq, d)).astype('float32')

# building index. IndexFlatL2 doesn't require training jus intialize with the vector dimension.
index = faiss.IndexFlatL2(d)

# add vectors to the index. Important notes are that each vector is sotred in the oder it was added and ID's are assigned as their position in the array.
index.add(xb)

# search for nearest neighbors. This will check each query in xq against every vector in the database or xb. D will be the top-k nearest neighbors for each query. I will contain the indices or ID's for each of said neighbors
start = time.time()
D, I = index.search(xq, k=5)
end = time.time()
print(f"Search time: {end - start:.4f} seconds")
print("Distances (D):")
display(D)
print("\nIndices (I):")
display(I)
# returns the indecies of the 5 most similar vectors in the database for each query

# COMPARISON to NumPy brute-force search; same math but is pure python 
# NumPy brute-force: manually compute L2 distance from each query to all 100k vectors
start = time.time()
for q in xq:
    diffs = xb - q                        # subtract query from every vector
    dists = np.sum(diffs ** 2, axis=1)    # square + sum = L2 distance
    top5 = np.argsort(dists)[:5]          # sort and grab top 5 indices
end = time.time()
print(f"NumPy brute-force time: {end - start:.4f} seconds")

'''
Notes:
 - Right now I am usign the brute-force or IndexFlatL2. This compares every query against the 100,000 vectors I had stored. At this scale there is no issue, but imagine an app with 10 million or billion vectors ( embeddings from documents, images, users, etc. ). Its obvious how slow that would be. So the trade off with IndexFlatL2 is that its 100% accurate but slow at scale. 
 - In the real world of AI, every app is essentially asking "which embeddings stored in this database are closest to the query embedding?" or nearest-neighbor search. FAISS makes that possible at scale.
 - Analyzing the times of brute-force NumPy versus the Faiss method, its clear that even with the same mathmatical operations and inputs, along with the same outputs, the FAISS is better at scale.
'''

'''
INDEXING TYPES:
  Flat (brute-force) indexes 
    - IndexFlatL2, IndexFlatIP, etc.
    - Stores every vectore and scans all of them
    - Is an exact search
    - Requires no training
    - Simple but slow for larger datasets

  IVF (inverted file) indexes
    - IndexIVFFlat, IndexIVFPQ, IndexIVFScalarQuantizer, etc.
    - Uses clustering to assign vectors to coarse "cells" and only search a subset of then
    - Trade recall is good for speed

  PQ / compressed indexes
    - IndexPQ, IndexLSH, residual / additive quantizer-based variants
    - The quantizer turns a long float vector into a short code so it takes less RAM and is faster to compare
    - Basically compresses vectors into short codes
    - Saves memory and speeds up distance computation

  HNSW (graph-based) indexes
    - IndexHNSWFlat, IndexHNSWPQ, etc.
    - Build a navigable small world graph over the vectors
    - Very fast approximate search
    - Higher memory overhead

  Binary indexes
    - IndexBinaryFlat, IndexBinaryIVF*, etc.
    - Work on binary vectors using Hamming distance
    - Used when data is already in binary form or heavily compressed.

  Composite / pipeline indexes
    - Mix of all types
'''
