# This is a function to ask a matrix to the user and shaping it.

import numpy as np

def ask_matrix():
    matrix = []
    el = float(input('Entrez le premier élément de la matrice : '))
    matrix.append(el)
    while el:
        el = input("Entrez l'élément suivant, appuyez sur enter si termniné: ")
        if el:
            matrix.append(float(el))
    return matrix

def create_matrix(M):
    matrix = M
    nb_columns = int(input('Entrez le nombre de colonnes : '))
    nb_rows = int(input('Entrez le nombre de lignes : '))
    return np.reshape(matrix, (nb_rows, nb_columns))


# Press the green button in the gutter to run the 1script.
if __name__ == '__main__':
    print(create_matrix(ask_matrix()))

