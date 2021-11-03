##Ex 3.4 EnoncéEcrivezun programme qui inverse une matrice par la méthode du pivot de Gauss-Jordan
# (vous aurez besoin des programmes des exercices 1 et 2 sous forme de fonction)
# (Vous trouverez une description complète de l’algorithme en pseudo-codesur la diapo suivante)
# (On cherche le max de la première colonne comme premier pivot et si il ne se trouve pas en a11,
# on l’y met en échangeant la ligne du max avec la première. On divise la ligne par la valeur du max pour obtenir 1,
# puis on s’occupe de a12et ainsi de suite on descend jusqu’au bout de la colonne, puis on passe à la colonne suivante on cherche le max,
# on le met par échange sur la diagonale et on s’occupe des valeurs du dessous et du dessus dans la colonne 2 et on passe à la colonne suivante etc.)

import numpy as np
from numpy import matrix
from enter_the_matrix import *
# A =np.array([[4, 2, 0],
#      [4, 1, 6],
#      [2, 8, 3]])

def gauss_jordan(M) :
    A = matrix(M[:])

    nb = A.shape[0]
    for i in range(nb) :

        p = i
        while p < nb and A[p, p] == 0:
            p = p+1
        if p != i:
            tmp = matrix(A[i:i+1, :])
            A[i:i + 1, :] = A[p:p + 1, :]
            A[p:p+1, :] = tmp

        A[i:i+1, :] = A[i:i+1, :] / A[i, i]

        for j in range(nb) :
            if j != i :
                A[j:j+1, :] -= A[j, i]*A[i:i+1, :]

    return A



def transvection(A, i, j, alpha):
    #x = -A[j, i] / A[i, i]
    A[j, :] = A[j, :] - alpha * A[i, :]
    return A
if __name__ == '__main__':
    A = create_matrix(ask_matrix())
    print(A)
    print('-------------------')
    print(gauss_jordan(A))

