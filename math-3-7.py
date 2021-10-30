##Ex 3.5 EnoncéEcrivezun programme qui calcule les solutions d’un système d’équation
# . Le programme demandera combien il y a de variables et combien d'équations.
# Si les deux chiffres sont différents, affichage d'un message d'erreur (lequel?)
# et arrêt ou bouclage du programme pour reposer la question. Ensuite,
# boucle pour introduire le coefficient de chaque variable, équation par équation,
# mise en forme de la matrice correspondante et résolution du système (en utilisant pour l’inversion de matrice nécessaire le résultat
# de l’exercice précédent avec affichage du résultat
import numpy as np
from numpy import matrix

A =np.array([[4, 2, 0],
     [4, 1, 6],
     [2, 8, 3]])

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
    print(A)
    print('-------------------')
    print(gauss_jordan(A))

