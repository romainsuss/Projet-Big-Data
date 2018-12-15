#!/usr/bin/env python

# Le fichier d'entrée est supposé avoir des lignes de la forme "A, i, j, x", où i est l'index de la ligne, j est l'index de la colonne et x est la valeur de la ligne i, de la colonne j de A. Entrées de A sont suivies par des lignes de la forme "B, i, j, x" pour la matrice B.
# On suppose que les dimensions de la matrice sont telles que le produit A * B existe.


# cat nomdufichier.in | python smarter_map.py nbr_ligne_A nb_col_B | sort -n | python smarter_reduce.py nb_colA_ligneB
 
import sys
import string
import numpy

taille_block_a = 20
taille_block_b = 20

# Nombre de ligne de A
nbr_ligne_A = int(sys.argv[1]) 

# Nombre de colonne de B
nb_col_B = int(sys.argv[2])


# Input qui vient de STDIN 
for line in sys.stdin:
    
  # On supprime les espaces de début et de fin
  line = line.strip()

  # On fractionne la ligne en un tableau de données d'entrée
  entree = line.split(",")
    
  # On définit la ligne, la colonne et la valeur pour cette entrée
  ligne = int(entree[1])
  colonne = int(entree[2])
  valeur = float(entree[3])

  # S'il s'agit d'une entrée dans la matrice A ...
  if (entree[0] == "A"):
    
    # Générer les paires clé-valeur nécessaires
    a_block = int(ligne / taille_block_a)
    for b_block in range(1 + int(nb_col_B / taille_block_b)):
      print('{0:d},{1:d}\tA,{2:d},{3:d},{4:f}'.format(a_block, b_block, ligne, colonne, valeur))

  # Sinon, s'il s'agit d'une entrée dans la matrice B ...
  else:
    
    # Générer les paires clé-valeur nécessaires
    b_block = int(colonne / taille_block_b)
    for k in range(1 + int(nbr_ligne_A / taille_block_a)):
      print('{0:d},{1:d}\tB,{2:d},{3:d},{4:f}'.format(k, b_block, ligne, colonne, valeur))

	
        
