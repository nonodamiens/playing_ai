# playing_ai
Entrainement d'IA à jouer

Cours de Thibault Neveu

En premier on va tester la value fonction
V(t0) = V(t0) + lr x ( V(t1) - V(t0) )
Modifie la valeur de l'état actuel en fonction de la valeur des états suivants

exemple
Etats possibles :

|t0|t1|t2|
|---|---|---|
|révision|dodo|+5|
|binouze|super_binouze|-5|
|binouze|révision_dodo|0|
|révision|grosse_révision|-1|

Initialisation des états à 0
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

Résumé/résultat/choix de l'agent :

agent   -> révision (0.187) -> dodo (1.25)              => +5
                            -> grosse_révision (-0.25)  => -1
        -> binouze (-0.312) -> super_binouze (-1.25)    => -5
                            -> révision_dodo (0)        =>  0