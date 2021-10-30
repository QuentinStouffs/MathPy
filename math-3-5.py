##Ex 3.5 Enoncé Ecrivezun programme qui calcule le déterminant d’une matrice par la méthode du pivot de Gauss-Jordan
# (vous aurez besoin des programmes des exercices 1 et 2 sous forme de fonction)


from numpy.linalg import *
from numpy import matrix

A =matrix([[1., 2., 3.],
     [4., 5., 6.],
     [7., 8., 1.]])

# A =matrix([[1., 2., 2., 2.],
#      [1., 3., -2., -1.],
#      [3., 5., 8., 8.]])

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

def pivot_gauss(M) :
    A = matrix(M[:])
    nb = A.shape[0]
    for i in range(nb) :
        for j in range(i+1, nb):
            A[j:j+1, :] -= (A[j,i]/A[i,i])*A[i:i+1, :]
    return A

def det_gauss(M) :
    #matrice carée?
    if M.shape[0] != M.shape[1]:
        raise "La matrice n'est pas carrée!"
    A = matrix(M[:])
    Mtx = pivot_gauss(A)

    p = 1
    for i in range(Mtx.shape[0]):
        p *= Mtx[i, i]

    return p

if __name__ == '__main__':
    print(A)
    print('-------------------')
    print(det(A))
    print('-------------------')
    print(det_gauss(A))

