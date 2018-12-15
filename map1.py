#!/usr/bin/env python


#Le fichier d'entré est supposé avoir des lignes de la forme "A, i, j, x", où i est l'index de la ligne, j est l'index de la colonne et x est la valeur de la ligne i, de la colonne j de A. Entrées de A sont suivies par des lignes de la forme "B, i, j, x" pour la matrice B.
#On suppose que les dimensions de la matrice sont telles que le produit A * B existe.


#cat 1.in | python naive_map.py 2 2 | sort -n | python naive_reduce.py 3

import sys
import string
import numpy

# Nombre de ligne de A
nb_ligne_A = int(sys.argv[1]) 

# Nombre de colonne de B
nb_col_B = int(sys.argv[2])


# Input qui vient de STDIN 
for line in sys.stdin:
    
  # On supprime les espaces de début et de fin
  line = line.strip()

  # On fractionne la ligne en un tableau de données d'entrée
  entré = line.split(",")
    
  # On définie la ligne, la colonne et la valeur pour cette entrée
  ligne = int(entré[1])
  colonne = int(entré[2])
  valeur = float(entré[3])

  # S'il s'agit d'une entrée dans la matrice A ...
  if (entré[0] == "A"):
		
    # Générer les paires clé-valeur nécessaires
    for i in range(nb_col_B):
      print('{0:d},{1:d}\tA,{2:d},{3:f}'.format(ligne, i, colonne, valeur))

  # Sinon, s'il s'agit d'une entrée dans la matrice B ...
  else:
		
    # On génére les paires clé-valeur nécessaires
    for i in range(nb_ligne_A):
      print('{0:d},{1:d}\tB,{2:d},{3:f}'.format(i, colonne, ligne, valeur))

# Input 
#A,0,0,2
#A,0,1,3
#A,0,2,1
#A,1,0,8
#A,1,1,10
#A,1,2,7
#B,0,0,5
#B,0,1,6
#B,1,0,8
#B,1,1,5
#B,2,0,10
#B,2,1,3


# Output mapper sort 
#0,0	A,0,2.000000
#0,0	A,1,3.000000
#0,0	A,2,1.000000
#0,0	B,0,5.000000
#0,0	B,1,8.000000
#0,0	B,2,10.000000
#0,1	A,0,2.000000
#0,1	A,1,3.000000
#0,1	A,2,1.000000
#0,1	B,0,6.000000
#0,1	B,1,5.000000
#0,1	B,2,3.000000
#1,0	A,0,8.000000
#1,0	A,1,10.000000
#1,0	A,2,7.000000
#1,0	B,0,5.000000
#1,0	B,1,8.000000
#1,0	B,2,10.000000
#1,1	A,0,8.000000
#1,1	A,1,10.000000
#1,1	A,2,7.000000
#1,1	B,0,6.000000
#1,1	B,1,5.000000
#1,1	B,2,3.000000

# Output reducer 
#(0,1),44.000000
#(1,0),12.000000
#(1,1),40.000000
#(1,1),48.000000
        
