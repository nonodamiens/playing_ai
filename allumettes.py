"""Jeu des allumettes"""

import re

# choix du nombre d'allumettes
nb_allumettes = input('Choisir le nombre d\'allumettes > 10 :')
# vérification de la cohérence de l'entrée
while not re.match(r'\d{2}', nb_allumettes):
    print('merci de choisir entre 10 et 100')
    nb_allumettes = input('nouveau choix du nombre d\'allumettes :')
nb_allumettes = int(nb_allumettes)
print('vous avez choisi:', nb_allumettes, 'allumettes')

# boucle de jeu
while nb_allumettes > 0:
    print('Il reste ', nb_allumettes, 'allumettes')
    # joueur 1
    j1 = input('j1 : Choisir 1, 2 ou 3 allumettes :')
    while j1 not in ['1', '2', '3']:
        j1 = input('j1 : Choisir 1, 2 ou 3 allumettes :')
    # on retire les allumettes
    nb_allumettes -= int(j1)
    # check si perdu
    if nb_allumettes <= 0:
        print('J1 a perdu')
    print('Il reste ', nb_allumettes, 'allumettes')
    # de même pour joueur2
    j2 = input('j2 : Choisir 1, 2 ou 3 allumettes :')
    while j2 not in ['1', '2', '3']:
        j2 = input('j2 : Choisir 1, 2 ou 3 allumettes :')
    # on retire les allumettes
    nb_allumettes -= int(j2)
    # check si perdu
    if nb_allumettes <= 0:
        print('J2 a perdu')
