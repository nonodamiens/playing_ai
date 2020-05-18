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

human = input('joueur 1 ia (0) ou humain (1)')
while human not in ['0', '1']:
    human = input('joueur 1 ia (0) ou humain (1)')
j1 = Gamer(int(human))
human = input('joueur 2 ia (0) ou humain (1)')
while human not in ['0', '1']:
    human = input('joueur 2 ia (0) ou humain (1)')
j2 = Gamer(int(human))

# boucle de jeu
go_on = True
while go_on:
# boucle de partie
    while jeu.nb_allumette > 0:
        print('Etat du jeu :')
        jeu.etat()
        # joueur 1
        print('Joueur 1')
        j1_choix = j1.action()
        if jeu.nb_allumette < 3:
            choix = [str(x) for x in range(1, jeu.nb_allumette + 1)]
        else:
            choix = ['1', '2', '3']
        while j1_choix not in choix:
            j1_choix = j1.action()
        # memorisation du choix
        j1.partie(j1_choix)
        # on retire les allumettes
        jeu.action(int(j1_choix))
        # check si perdu
        if jeu.fin():
            j1.nb_perte += 1
            j2.nb_gain += 1
            print('J1 a perdu')
            break
        # de même pour joueur2
        jeu.etat()
        print('Joueur 2')
        j2_choix = j2.action()
        if jeu.nb_allumette < 3:
            choix = [str(x) for x in range(1, jeu.nb_allumette + 1)]
        else:
            choix = ['1', '2', '3']
        while j2_choix not in choix:
            j2_choix = j2.action()
        # memorisation du choix
        j2.partie(j2_choix)
        # on retire les allumettes
        jeu.action(int(j2_choix))
        # check si perdu
        if jeu.fin():
            j2.nb_perte += 1
            j1.nb_gain += 1
            print('j2 a perdu')
    print('coups de j1 :', j1.partie_mem)
    print('coups de j2 :', j2.partie_mem)
    # une nouvelle partie
    restart = input('Un nouvelle partie ? (y/n)')
    while restart not in ['y', 'n']:
        restart = input('Un nouvelle partie ? (y/n)')
    if restart == 'n':
        go_on = False
    jeu.reset()
    j1.reset()
    j2.reset()

print('J1 a perdu', j1.nb_perte, 'fois et gagné', j1.nb_gain, 'fois.')
print('J2 a perdu', j2.nb_perte, 'fois et gagné', j2.nb_gain, 'fois.')