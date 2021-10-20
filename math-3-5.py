##Ex 3.4 Enoncé Ecrivez un programme qui soustrait d'une ligne k un multiple d'une
# autre ligne d'une matrice (transvection: Lk= Lk-alpha*Li) et qui  sera appelé par
# l'instruction nom-fonction(A,k,i,alpha) où A est  le nom de la matrice et k et i
# le numéro des lignes à soustraire et  alpha le facteur de multiplication de la ième
# ligne avant soustraction

import numpy as np

A =np.array([[4, 2, 0],
     [4, 1, 6],
     [2, 8, 3]])

def transvection(A, i, j, alpha):
    #x = -A[j, i] / A[i, i]
    A[j, :] = A[j, :] - alpha * A[i, :]
    return A
if __name__ == '__main__':
    print(A)
    print('-------------------')
    print(transvection(A, 2, 1, 12))

