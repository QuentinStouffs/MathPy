from math import *
import numpy as np

M= np.matrix([[4.1, 2.0, 0],
    [4.6, 1, 6],
    [2, 8, 3]])
 
print('ex1')
print( M.item((1,2)) )
print('-------')

print('ex2')
print( M[1] )
print('-------')

print('ex3')
print( M[:,0] )
print('-------')

print('ex4')
Z = np.eye(3, dtype=int)
print(Z)
print('-------')

print('ex5')
Z = np.eye(5)
print(Z)
print('-------')

print('ex6')
A = np.mat([2, 4, 6, 12, 24, 36])
print(A.reshape(3,2))
print('-------')
