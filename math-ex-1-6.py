import numpy as np
import sys

# etape 0: Lancer le Programme
# print("**********************************************************")
# print("****************** Les matrices en s'amusant *************")
# print("**********************************************************")
# print("\n")
# print("...")
# print("Bonjour l'ami... Toi tu as une tête à être là pour faire des maths...")
# answer = input("j'ai raison ? O/n \n")
# if answer.lower() == "o":
# 	print("Yay, je le savais. Tu verras ça va être fun! ")
# else:
# 	print("Oh... ok. Je pensais que tu étais un mec cool.")
# 	print("Bonne journée..")
# 	quit()

# etape 1: demander à l'utilisateur de rentrer taille de la matrice A
print("Parfait, commençons.\n")
input_matrice_A = input("Tout d'abord, quelle est la taille de ta matrice A? (exemple: 2x3)\n")
diva1 = int(input_matrice_A[0])
diva2 = int(input_matrice_A[2])
# etape 2: demander à l'utilisateur de rentrer les données de la matrice A
print("Super ! Tu t'en sors bien. Maintenant écris tous les éléments de cette matrice en les séparants par un espace.")
print("Si ce sont des float, n'oublie pas que le séparateur est un point.")
data_matrice_A = input(f"Avant de valider, vérifie qu'il y a bien {diva1*diva2} éléments\n")

# etape 3: demander à l'utilisateur de rentrer taille de la matrice B
input_matrice_B = input("Ok. Maintenant on fait pareil avec la matrice B. Taille? (exemple: 2x3)\n")
divb1 = int(input_matrice_B[0])
divb2 = int(input_matrice_B[2])
# etape 4: demander à l'utilisateur de rentrer les données de la matrice B
print("Maintenant écris tous les éléments de cette matrice.")
data_matrice_B = input(f"N'oublie pas de vérifier qu'il y a bien {divb1*divb2} éléments\n")

# etape 5: afficher les deux matrices
print("Voici la matrice A")
a = data_matrice_A.split(" ")
if data_matrice_A.find(".") == -1: # vérifie entier ou float
	lista = list(map(int, a))
	a = np.asarray(lista,dtype=int).reshape(int(input_matrice_A[0]), int(input_matrice_A[2]))
	
else:
	lista = list(map(float, a))
	a = np.asarray(lista,dtype=float).reshape(int(input_matrice_A[0]), int(input_matrice_A[2]))
print(a)


print("Voici la matrice B")
b = data_matrice_B.split(" ")
if data_matrice_B.find(".") == -1: # vérifie entier ou float
	listb = list(map(int, b))
	b = np.asarray(listb,dtype=int).reshape(int(input_matrice_B[0]), int(input_matrice_B[2]))
	
else:
	listb = list(map(float, b))
	b = np.asarray(listb,dtype=float).reshape(int(input_matrice_B[0]), int(input_matrice_B[2]))
print(b)


# etape 6: calculer le produit matriciel de A par B et B par A et indiquer quand ce n'est pas possible et pourquoi
print("Ok maintenant qu'on a nos matrices, il serait intéressant de travailler dessus, qu'en penses-tu ?")
print("en fait t'as pas le choix !")
print("commençons par le produit matriciel de A par B")
try:
	print(np.matmul(a, b))
except ValueError as err:
	print("Tu ne peux pas faire ça: {0}".format(err))
except:
	print("une erreur s'est produite: ", sys.exc_info([0]))

print("Et plus fort encore, on fait le produit matriciel de B par A maintenant")
try:
	print(np.matmul(b, a))
except ValueError as err:
	print("Tu ne peux pas faire ça: {0}".format(err))
except:
	print("une erreur s'est produite: ", sys.exc_info([0]))

# etape 7: calculer la somme de A+B et indiquer quand ce n'est pas possible et pourquoi
print("Ok good ! Maintenant on va faire la somme de A et B")
try:
	print(a+b)
except ValueError as err:
	print("Tu ne peux pas faire ça: {0}".format(err))
except:
	print("une erreur s'est produite: ", sys.exc_info([0]))

# etape 8: calculer et afficher la transposée de A en indiquant son nombre de lignes et de colonnes
print("Dernière étape: On va transposer la matrice A. Tu es prêt ?")
try:
	c = np.transpose(a)
	print(c)
	result = c.shape
	print(f"Il y a {result[0]} lignes et {result[1]} colonnes")
except ValueError as err:
	print("Tu ne peux pas faire ça: {0}".format(err))
except:
	print("une erreur s'est produite: ", sys.exc_info([0]))