import numpy as np
import time

distance = lambda a,b: np.sum(np.dot((a-b),(a-b)))**0.5

X = np.random.random((100,100))

start = time.time()
dist = np.zeros([100,100])
for i in range(0,100):
    for j in range (0,100):
        dist[i,j] = distance(X[i],X[j])
        
print("Time to compute 100 distance between 100-d objects: {}s.".format(time.time() - start))


	

import math


""" Super simple example"""
# defines function consisely
function = lambda x: x**2 - 5
print(function(4))


"""
maps each input in input to the function specified by lambda, in this case exp(x)+10
(where the first x before the : denotes that x is the input) and formats this map as a readable list
"""
input = [1,2,3,4,5,6,7,8,9,10,0]
print(list(map(lambda x: math.exp(x)+10,input))) 
