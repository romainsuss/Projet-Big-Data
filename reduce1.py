#!/usr/bin/env python


#cat 1.in | python naive_map.py 2 2 | sort -n | python naive_reduce.py 3

import sys
import string
import numpy

# Nombre de colonnes de A / lignes de B
nb_colA_ligneB = int(sys.argv[1]) 


# On créer des structures de données pour contenir les valeurs de ligne / colonne actuelles
current_clé = None
current_res = 0.0
valeur_dict = dict()

# Entré qui vient de STDIN 
for line in sys.stdin:

  # On supprime les espaces de début et de fin 
  line = line.strip()
    
  # On recupère clé/valeur
  clé, valeur = line.split('\t',1)  # clé : 0,0	 valeur : A,0,2.000000
  
  
  # On analyse l'entré clé/valeur  
  try:
    ligne, colonne = map(int, clé.split(','))
    valeur = valeur.split(',')
    clé = (ligne, colonne)  
    replicate_clé, element_valeur = int(valeur[1]), float(valeur[2])
    
#    print('clé =', clé) # (0, 0)
#    print('replicate_clé =', replicate_clé) # 0
#    print('element_valeur =', element_valeur) # 2.0000
#    print('current clé =' ,current_clé )
#    print()
    
  except:
    continue

  # Si nous sommes toujours sur la même clé ...
  if clé == current_clé:
    
    # On process la paire clé/valeur 
    if replicate_clé not in valeur_dict:
      valeur_dict[replicate_clé] = [element_valeur]
    else:
      valeur_dict[replicate_clé].append(element_valeur)

  # Sinon, s'il s'agit d'une nouvelle clé ...
  else:
    
    # S'il s'agit d'une nouvelle clé et non de la première clé que nous avons vue
    if current_clé:
      
      # On calcule / affiche le résultat dans STDOUT
      for j in range(nb_colA_ligneB):
        if (j in valeur_dict) and (len(valeur_dict[j]) == 2):
            #print('valeur_dict = ' , valeur_dict)
            current_res += valeur_dict[j][0] * valeur_dict[j][1]
      print ('({0:d},{1:d}),{2:f}'.format(ligne, colonne, current_res))
  
    current_clé = clé
    valeur_dict = dict()
    
    # On process input pour une nouvelle clé
    valeur_dict[replicate_clé] = [element_valeur]
    current_res = 0.0


# On calcule / affiche le résultat pour la dernière clé 
if current_clé:
  for j in range(nb_colA_ligneB):
    if (j in valeur_dict) and (len(valeur_dict[j]) == 2):
      current_res += valeur_dict[j][0] * valeur_dict[j][1]
  print('({0:d},{1:d}),{2:f}'.format(ligne, colonne, current_res))

 
  
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

