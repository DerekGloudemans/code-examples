

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