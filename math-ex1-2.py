from math import *
import numpy as np

A= [[1,2,3],[4,5,6],[7,8,9]]
B= [[9,9,9],[9,9,9],[9,9,9]]

print('ex1')
print(A + B)
print('-------')

print('ex2')

Z = []
for i in range(len(A)):
    C = []
    for j in range(len(A[i])):
        C.append(A[i][j] + B[i][j])
    Z.append(C)

print(Z)

print('-------')
