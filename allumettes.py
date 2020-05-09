"""Jeu des allumettes"""

from classes import *

import re

# choix du nombre d'allumettes
nb_allumettes = input('Choisir le nombre d\'allumettes > 10 :')
# vérification de la cohérence de l'entrée
while not re.match(r'\d{2}', nb_allumettes):
    print('merci de choisir entre 10 et 100')
    nb_allumettes = input('nouveau choix du nombre d\'allumettes :')
nb_allumettes = int(nb_allumettes)
print('vous avez choisi:', nb_allumettes, 'allumettes')

# Instanciation du jeu
jeu = Game(nb_allumettes)

print('jeu :', jeu.nb_allumette)

# boucle de jeu
while jeu.nb_allumette > 0:
    print('Etat du jeu :')
    jeu.etat()
    # joueur 1
    j1 = input('j1 : Choisir 1, 2 ou 3 allumettes :')
    if jeu.nb_allumette < 3:
        choix = [str(x) for x in range(1, jeu.nb_allumette + 1)]
    else:
        choix = ['1', '2', '3']
    while j1 not in choix:
        j1 = input('j1 : Choisir 1, 2 ou 3 allumettes :')
    # on retire les allumettes
    jeu.action(int(j1))
    # check si perdu
    if jeu.fin():
        print('J1 a perdu')
        break
    # de même pour joueur2
    jeu.etat()
    j2 = input('j2 : Choisir 1, 2 ou 3 allumettes :')
    if jeu.nb_allumette < 3:
        choix = [str(x) for x in range(1, jeu.nb_allumette + 1)]
    else:
        choix = ['1', '2', '3']
    while j2 not in choix:
        j2 = input('j2 : Choisir 1, 2 ou 3 allumettes :')
    # on retire les allumettes
    jeu.action(int(j2))
    # check si perdu
    if jeu.fin():
        print('J2 a perdu')
