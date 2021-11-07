#-*- coding: utf8 -*-

# La première ligne indique le type d'encodage utilisé.

#----------------------------------------------------------------------#
#                                                                      #
#                 Cours de Mathématiques pour BAC Info                 #
#                            G. Barmarin                               #
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                                                                      #
#                           Ex 2.1 Enoncé                              #
#                                                                      #
#   Numpy et PIL: ouverture d'une image, transformation en tableau,    #
#         traitement et enregistrement de la nouvelle image            #                                                          
#                                                                      #
#----------------------------------------------------------------------#

#-----------------------------------------------------------------------
# Importation des bibliothèques
#-----------------------------------------------------------------------

import csv
import time
from tkinter import *
from PIL import Image, ImageDraw
import numpy as np

#-----------------------------------------------------------------------
# encodage des fonctions 
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# encodage du programme principal
#-----------------------------------------------------------------------

print("Utilisation de numpy et de PIL")
print("------------------------------")
print("Utilisation des arrays pour traiter des images\n")

# On charge l'image Lenna.jpg ou une image alternative xxx.jpg si on la trouve trop sexiste
# et on la transforme en un tableau nommé image contenant les couleurs

nom='Lenna512'
image_entree = Image.open(nom +".png")
image = np.asarray(image_entree)
nb_lignes = image.shape[0]
nb_colonnes = image.shape[1]
print("\nVous avez ouvert l'image ", nom, ".png\n")
print("qui a pour dimensions ", nb_lignes,"lignes et ", nb_colonnes, " colonnes\n")

# On crée notre image de sortie sous forme de tableau numpy (ici on fait juste une copie de l'image originale)

image_sortie = np.copy(image)

# On sauvegarde les images pour pouvoir les afficher et tester le résultat

Image.fromarray(image).save("image_entree.png")							# Image originale
Image.fromarray(image_sortie).save("image_sortie.png")                  # Image modifiée
