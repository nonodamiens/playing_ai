"""Les classes de jeu des allumettes"""
import random

class Game:
    """Classe de définition du jeu (nombre d'allumettes...)"""

    def __init__(self, nb):
        """Instanciation d'une partie"""
        self.nb_allumette_initial = nb
        self.nb_allumette = nb

    def fin(self):
        if self.nb_allumette <= 0:
            return True
        else:
            return False
    
    def reset(self):
        self.nb_allumette = self.nb_allumette_initial
        return self.nb_allumette
    
    def etat(self):
        print('|' * self.nb_allumette, '(', self.nb_allumette, ')')

    def action(self, choix_nb):
        """Action de jeu, on retire le nombre d'allumettes choisi par le joueur au nombre total d'allumettes"""
        self.nb_allumette -= choix_nb

class Gamer:
    """Classe de définition d'un joueur"""

    def __init__(self, human):
        """Instanciation d'un joueur"""
        self.human = human
        self.partie_mem = []
        self.choix_valeur = []
        self.etats = {}
        self.resultat = 0
        self.nb_gain = 0
        self.nb_perte = 0
        self.lr = 0.1

    def reset(self):
        """Remise à zéro des stats du joueur"""
        # self.nb_gain = 0
        # self.nb_perte = 0
        self.partie_mem = []
    
    def action(self):
        """Choix du nombre d'allumette à prendre - choix du joueur humain ou non"""
        if self.human:
            choix = input('Choix d\'1, 2 ou 3 allumettes :')
            return choix
        else:
            choix = str(random.randint(1,3))
            return choix

    def partie(self, coup):
        """Memorisation des coups joués"""
        self.partie_mem.append(coup)

    # def etat(self, nb_allumette):
    #     """Enregistrement des différents états de la partie"""
    #     if nb_allumette in self.etats:
    #         print('toto')
    #     else:
    #         self.etats[nb_allumette] = 0

    def value_fonction(self, etats, resultat):
        """Calcul de la value fonction - gagné = 1 / perdu = 0"""
        if etats[-1] not in self.etats:
            self.etats[etats[-1]] = self.lr * resultat
        else:
            self.etats[etats[-1]] = self.etats[etats[-1]] + self.lr * (resultat - self.etats[etats[-1]])
        for i in range(len(etats) - 1):
            if etats[-2 - i] not in self.etats:
                self.etats[etats[-2 -i]] = self.lr * self.etats[etats[-1 -i]]
            else:
                self.etats[etats[-2 -i]] = self.etats[etats[-2 -i]] + self.lr * (self.etats[etats[-1 -i]] - self.etats[etats[-2 -i]])
