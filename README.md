# playing_ai #
Projet d'entrainement d'IA à jouer

Ce projet se base sur les Cours de Thibault Neveu
https://www.youtube.com/channel/UCVso5UVvQeGAuwbksmA95iA

## contenu ##
Ce projet contient un notebook allumettes.py qui explique pas à pas comment coder et entrainer des IA au jeu des allumettes. Une façon simple d'entrer dans le monde du reinforcement learning.

Il contient également le jeu des allumettes et l'entrainement d'IA packagé pour s'amuser.

## value function ##
La *value function* est la fonction de base utilisée en *reinforcement learning*. Pour mieux l'appréhender, voici un petit exemple tirer du cours de Thibaut Neveu

### Formalisation de la value function ###

V(t<sub>0</sub>) = V(t<sub>0</sub>) + lr * (V(t<sub>1</sub>) - V(t<sub>0</sub>))

Elle sert à modifier la valeur de l'état actuel en fonction de la valeur des états suivants

### exemple ###

* Etats possibles :

|t0|t1|t2|
|---|---|---|
|révision|dodo|+5|
|binouze|super_binouze|-5|
|binouze|révision_dodo|0|
|révision|grosse_révision|-1|

* Initialisation des états à 0

Calcul de la valeur des différents états avec la value function :
(on part de la fin, retropropagation)

lr = 0.5

t2->t1:
|t2|t1|
|---|---|
|0 + 0.5 * (5 - 0) = 2.5|0 + 0.5 * (2.5 - 0) = 1.25 -> dodo|
|0 + 0.5 * (-5 - 0) = -2.5|0 + 0.5 * (-2.5 - 0) = -1.25 -> super_binouze|
|0 + 0.5 * (0 - 0) = 0|0 + 0.5 * (0 - 0) = 0 -> révision_dodo|
|0 + 0.5 * (-1 - 0) = -0.5|0 + 0.5 * (-0.5 - 0) = -0.25 -> grosse_révision|

t1 -> t0
|t1|t0|
|---|---|
|1.25|0 + 0.5 * (1.25 - 0) = 0.625 -> révision|
|-1.25|0 + 0.5 * (-1.25 - 0) = -0.625 -> binouze|
|0|**-0.625** + 0.5 * (0 - **-0.625**) = **-0.312** -> binouze|
|-0.25|**0.625** + 0.5 * (-0.25 - **0.625**) = **0.187** -> révision|

* Résumé/résultat/choix de l'agent :

agent   -> révision (0.187) -> dodo (1.25)              => +5

                            -> grosse_révision (-0.25)  => -1

        -> binouze (-0.312) -> super_binouze (-1.25)    => -5

                            -> révision_dodo (0)        =>  0