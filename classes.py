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
        self.nb_gain = 0
        self.nb_perte = 0

    def reset(self):
        """Remise à zéro des stats du joueur"""
        self.nb_gain = 0
        self.nb_perte = 0
    
    def action(self):
        """Choix du nombre d'allumette à prendre - choix du joueur humain ou non"""
        if self.human:
            choix = input('Choix d\'1, 2 ou 3 allumettes :')
            return choix
        else:
            choix = str(random.randint(1,3))
            return choix
    