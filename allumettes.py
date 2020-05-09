"""Jeu des allumettes"""

import re

# choix du nombre d'allumettes
nb_allumettes = input('Choisir le nombre d\'allumettes > 10 :')
# vérification de la cohérence de l'entrée
while not re.match(r'\d{2}', nb_allumettes):
    print('merci de choisir entre 10 et 100')
    nb_allumettes = input('nouveau choix du nombre d\'allumettes :')

print('vous avez choisi:', nb_allumettes, 'allumettes')