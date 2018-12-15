#!/usr/bin/env python

#cat nomdufichier.in | python smarter_map.py nbr_ligne_A nb_col_B | sort -n | python smarter_reduce.py nb_colA_ligneB

import sys
import string
import numpy

taille_block_a = 20
taille_block_b = 20

# Nombre de colonnes de A / lignes de B
nb_colA_ligneB = int(sys.argv[1])


# calcule et affiche les résultats

def CalculerElem(clé_actuelle, val_a, val_b):
  # on charge le nombre de block
  a_block, b_block = clé_actuelle[0], clé_actuelle[1]
  # la fourchette de l'indice qui implique le calcul
  min_a = taille_block_a * a_block
  max_a = min(taille_block_a * (1+a_block) - 1, a_scale)
  min_b = taille_block_b * b_block
  max_b = min(taille_block_b * (1+b_block) - 1, b_scale)
  # compute/output result
  for a1 in range(max_a - min_a + 1):
    for b1 in range(max_b - min_b + 1):
      a = min_a + a1
      b = min_b + b1
      res_actuelle = 0
      for j in range(nb_colA_ligneB):
        res_actuelle += val_a[a][j] * val_b[j][b]
      print('({0:d},{1:d}),{2:f}'.format(a, b, res_actuelle))

# On crée des structures de données pour contenir les valeurs de ligne / colonne actuelles
clé_actuelle = None
res_actuelle = 0
val_a, val_b = dict(), dict()
a_scale, b_scale = 0, 0

# Entrée qui vient de STDIN
for line in sys.stdin:

  # On supprime les espaces de début et de fin 
  line = line.strip()
    
  # On recupère clé/valeur
  clé, valeur = line.split('\t',1)
  
  # On analyse l'entrée clé/valeur 
  try:
    clé = tuple(map(int, clé.split(',')))
    valeur = valeur.split(',')
    matrice = valeur[0]
    ligne, colonne, valeur = int(valeur[1]), int(valeur[2]), float(valeur[3])
    
    #print('clé =', clé) 
    #print('valeur =' ,valeur)
    #print('matrice = ',matrice, '\n')
    
  except:
    continue

  #si on est encore sur la même clé
  if clé == clé_actuelle:
    
    #On process la paire clé/valeur
    if matrice == 'A':
      #process pour la matrice A
      if ligne not in val_a:
          val_a[ligne] = dict()
      val_a[ligne][colonne] = valeur
      a_scale = max(a_scale, ligne)
      #print('A : val a : ', val_a, 'a scale : ',a_scale)
    else:
      #process pour la matrice B
      if ligne not in val_b:
          val_b[ligne] = dict()
      val_b[ligne][colonne] = valeur
      b_scale = max(b_scale, colonne)
      #print('B : val b : ', val_a, 'b scale : ',b_scale, '\n')

  #si on change de clé
  else:
    
    #si nouvelle clé mais pas la première
    if clé_actuelle:
      
      #calcule et affiche les résultats
      CalculerElem(clé_actuelle, val_a, val_b)

    clé_actuelle = clé
    res_actuelle = 0
    a_scale, b_scale = 0, 0
    val_a, val_b = dict(), dict()
    
    #On process la paire clé/valeur
    if matrice == 'A':
      #process pour la matrice A
      if ligne not in val_a:
          val_a[ligne] = dict()
      val_a[ligne][colonne] = valeur
      a_scale = max(a_scale, ligne)
      #print('A : val a : ', val_a, 'a scale : ',a_scale)
    else:
      #process pour la matrice B
      if ligne not in val_b:
          val_b[ligne] = dict()
      val_b[ligne][colonne] = valeur
      b_scale = max(b_scale, colonne)
      #print('B : val b : ', val_a, 'b scale : ',b_scale, '\n')
      
#calcule et affiche les résultats pour la dernière clé
if clé_actuelle:
  
  #calcule et affiche les résultats
  CalculerElem(clé_actuelle, val_a, val_b)


