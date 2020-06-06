"""Jeu des allumettes"""

from allumettes.classes.game import Game
from allumettes.classes.gamer import Gamer
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

# Choisir le nombre d'entrainement de l'IA de 0 à 100000
training = input('Entrainez l\'IA, nombre de cycle ? ')
if training.isdigit():
    while int(training) < 0 or int(training) > 100000:
        training = input('Entrainez l\'IA, nombre de cycle ? ')
training = int(training)

# Instanciation des joueurs
ia1 = Gamer(0)
ia2 = Gamer(0)
humain = Gamer(1)

# Initialisation de la valeur des différents états du jeu
valeur_etats = {1:-1}
for etat in range(2, nb_allumettes + 1):
    valeur_etats[etat] = 0

# Initialisation des variables
lr = 0.01
greedy = 0.99

# Boucle d'entrainement
while training > 0:
    ia1_etats, ia2_etats = [], []
    while jeu.nb_allumette > 0:
        if jeu.fin():
            ia1.nb_perte += 1
            ia2.nb_gain += 1
            ia1.resultat = -1
            ia2.resultat = 1
            break

        if jeu.nb_allumette > 3:
            ia1_choix = ia1.action(3, greedy, [valeur_etats[i] for i in range(jeu.nb_allumette - 3, jeu.nb_allumette)])
        else:
            ia1_choix = ia1.action(jeu.nb_allumette, greedy, [valeur_etats[i] for i in range(1, jeu.nb_allumette)])
        ia1.partie(ia1_choix)
        ia1_etats.append(jeu.nb_allumette)
        jeu.action(int(ia1_choix))
        
        if jeu.fin():
            ia2.nb_perte += 1
            ia1.nb_gain += 1
            ia2.resultat = -1
            ia1.resultat = 1
            break

        if jeu.nb_allumette > 3:
            ia2_choix = ia2.action(3, greedy, [valeur_etats[i] for i in range(jeu.nb_allumette - 3, jeu.nb_allumette)])
        else:
            ia2_choix = ia2.action(jeu.nb_allumette, greedy, [valeur_etats[i] for i in range(1, jeu.nb_allumette)])
        ia2.partie(ia2_choix)
        ia2_etats.append(jeu.nb_allumette)
        jeu.action(int(ia2_choix))

    # actualisation des valeur d'états avec les value fonction
    valeur_etats[ia1_etats[-1]] = valeur_etats[ia1_etats[-1]] + lr * (ia1.resultat - valeur_etats[ia1_etats[-1]])
    valeur_etats[ia2_etats[-1]] = valeur_etats[ia2_etats[-1]] + lr * (ia2.resultat - valeur_etats[ia2_etats[-1]])
    for i in range(len(ia1_etats) - 1):
        v_n = valeur_etats[ia1_etats[-2 -i]]
        v_n_1 = valeur_etats[ia1_etats[-1 -i]]
        valeur_etats[ia1_etats[-2 -i]] = v_n + lr * (v_n_1 - v_n)
    for i in range(len(ia2_etats) - 1):
        v_n = valeur_etats[ia2_etats[-2 -i]]
        v_n_1 = valeur_etats[ia2_etats[-1 -i]]
        valeur_etats[ia2_etats[-2 -i]] = v_n + lr * (v_n_1 - v_n)

    # Diminution de l'exploration toutes les 10 parties
    training -= 1
    if training % 10 == 0:
        greedy = max(greedy * 0.99, 0.05)
    
    jeu.reset()
    ia1.reset()
    ia2.reset()

# Fin de l'ntrainement, affichage de quelques éléments de résultat
print('liste des valeur par états :')
for v in valeur_etats:
    print(v, ':', valeur_etats[v])
print('ratio des parties')
print('joueur 1 winrate :', ia1.winrate())     
print('joueur 2 winrate :', ia2.winrate())

# boucle de jeu trained IA vs lambda IA
ial = Gamer(0)

print('combat ia entrainée vs ia lambda')
nb_parties = input('Combien de parties ? :')
while nb_parties.isdigit() == False:
    nb_parties = input('Combien de parties ? :')
while int(nb_parties) < 0 or int(nb_parties) > 100000:
    nb_parties = input('Combien de parties ? :')
nb_parties = int(nb_parties)

# reset stats and game
ia1.nb_gain = 0
ia1.nb_perte = 0
jeu.reset()

greedy = 0.05
while nb_parties > 0:
    while jeu.nb_allumette > 0:
        if jeu.fin():
            ia1.nb_perte += 1
            ial.nb_gain += 1
            ia1.resultat = -1
            ial.resultat = 1
            break
        if jeu.nb_allumette > 3:
            ia1_choix = ia1.action(3, greedy, [valeur_etats[i] for i in range(jeu.nb_allumette - 3, jeu.nb_allumette)])
        else:
            ia1_choix = ia1.action(jeu.nb_allumette, greedy, [valeur_etats[i] for i in range(1, jeu.nb_allumette)])
        ia1.partie(ia1_choix)
        ia1_etats.append(jeu.nb_allumette)
        jeu.action(int(ia1_choix))
        
        if jeu.fin():
            ial.nb_perte += 1
            ia1.nb_gain += 1
            ial.resultat = -1
            ia1.resultat = 1
            break
        if jeu.nb_allumette > 3:
            ial_choix = ial.action(3, greedy, [valeur_etats[i] for i in range(jeu.nb_allumette - 3, jeu.nb_allumette)])
        else:
            ial_choix = ial.action(jeu.nb_allumette, greedy, [valeur_etats[i] for i in range(1, jeu.nb_allumette)])
        jeu.action(int(ial_choix))
    
    nb_parties -= 1

print('ratio des parties')
print('joueur ia1 winrate :', ia1.winrate())     
print('joueur ial winrate :', ial.winrate())

# boucle de jeu avec humain (to complete)
# go_on = False

# while go_on:
# # boucle de partie
# # initialisation des etats des joueurs
#     j1_etats = []
#     j2_etats = []
#     while jeu.nb_allumette > 0:
#         print('Etat du jeu :')
#         jeu.etat()
#         # joueur 1
#         print('Joueur 1')
#         j1_choix = j1.action()
#         if jeu.nb_allumette < 3:
#             choix = [str(x) for x in range(1, jeu.nb_allumette + 1)]
#         else:
#             choix = ['1', '2', '3']
#         while j1_choix not in choix:
#             j1_choix = j1.action()
#         # memorisation du choix et de l'etat
#         j1.partie(j1_choix)
#         j1_etats.append(jeu.nb_allumette)
#         # on retire les allumettes
#         jeu.action(int(j1_choix))
#         # check si perdu
#         if jeu.fin():
#             j1.nb_perte += 1
#             j2.nb_gain += 1
#             j1.resultat = -1
#             j2.resultat = 1
#             print('J1 a perdu')
#             break
#         # de même pour joueur2
#         jeu.etat()
#         print('Joueur 2')
#         j2_choix = j2.action()
#         if jeu.nb_allumette < 3:
#             choix = [str(x) for x in range(1, jeu.nb_allumette + 1)]
#         else:
#             choix = ['1', '2', '3']
#         while j2_choix not in choix:
#             j2_choix = j2.action()
#         # memorisation du choix et de l'etat
#         j2.partie(j2_choix)
#         j2_etats.append(jeu.nb_allumette)
#         # on retire les allumettes
#         jeu.action(int(j2_choix))
#         # check si perdu
#         if jeu.fin():
#             j2.nb_perte += 1
#             j1.nb_gain += 1
#             j1.resultat = 1
#             j2.resultat = -1
#             print('j2 a perdu')
    
#     # actualisation des valeur d'états avec les value fonction
#     valeur_etats[j1_etats[-1]] = valeur_etats[j1_etats[-1]] + lr * (j1.resultat - valeur_etats[j1_etats[-1]])
#     valeur_etats[j2_etats[-1]] = valeur_etats[j2_etats[-1]] + lr * (j2.resultat - valeur_etats[j2_etats[-1]])
#     for i in range(len(j1_etats) - 1):
#         valeur_etats[j1_etats[-2 -i]] = valeur_etats[j1_etats[-2 -i]] + lr * (valeur_etats[j1_etats[-1 -i]] - valeur_etats[j1_etats[-2 -i]])
#     for i in range(len(j2_etats) - 1):
#         valeur_etats[j2_etats[-2 -i]] = valeur_etats[j2_etats[-2 -i]] + lr * (valeur_etats[j2_etats[-1 -i]] - valeur_etats[j2_etats[-2 -i]])

#     print('liste des valeur par états :')
#     for v in valeur_etats:
#         print(v, ':', valeur_etats[v])
#     # j1.value_fonction(j1_etats, j1.resultat)
#     # j2.value_fonction(j2_etats, j2.resultat)
#     print('coups de j1 :', j1.partie_mem)
#     print('coups de j2 :', j2.partie_mem)
#     print('liste des etats j1', sorted(j1.etats.items(), reverse=True))
#     print('liste des etats j2', sorted(j2.etats.items(), reverse=True))
#     # une nouvelle partie
#     restart = input('Un nouvelle partie ? (y/n)')
#     while restart not in ['y', 'n']:
#         restart = input('Un nouvelle partie ? (y/n)')
#     if restart == 'n':
#         go_on = False
#     jeu.reset()
#     j1.reset()
#     j2.reset()

# # print('J1 a perdu', j1.nb_perte, 'fois et gagné', j1.nb_gain, 'fois.')
# print('J2 a perdu', j2.nb_perte, 'fois et gagné', j2.nb_gain, 'fois.')
quit()