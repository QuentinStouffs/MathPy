from math import *
import numpy as np

A= np.matrix([[4.1, 2.0, 0],
            [4.6, 1, 6],
            [2, 8, 3]])

B= np.matrix([[1, 1, 0],
            [1.0, 1, 1],
            [2, 2, 2]])

C= np.matrix([[1, 2],
              [0, 1],
              [3, 1]])

print('ex1')
print( A )
print( B )
print( C )

print('-------')

print('ex2')
print( A * B )
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
