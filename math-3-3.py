##Ex 3.3 Enoncé Ecrivez un programme qui inverse deux lignes d'une matrice et qui
# sera appelé par l'instruction nom-fonction(A,i,j)
# où A est le nom  de la matrice et i et j le numéro des lignes à échanger

from math import *
import numpy as np

A =np.array([[4, 2, 0],
     [4, 1, 6],
     [2, 8, 3]])

def swapRow(A, row1, row2):
    A[[row1, row2]] = A[[row2, row1]]
    return A
if __name__ == '__main__':
    print(A)
    print('-------------------')
    print(swapRow(A, 0, 2))

