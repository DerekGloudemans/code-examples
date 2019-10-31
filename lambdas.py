import numpy as np
import time

def distance(a,b):
    return np.sum(np.dot((a-b),(a-b)))**0.5

X = np.random.random((100,100))

start = time.time()
dist = np.zeros([100,100])
for i in range(0,100):
    for j in range (0,100):
        dist[i,j] = distance(X[i],X[j])
        
print("Time to compute 100 distance between 100-d objects: {}s.".format(time.time() - start))