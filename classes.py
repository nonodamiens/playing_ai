"""Les classes de jeu des allumettes"""

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

    def __init__(self):
        """Instanciation d'un joueur"""
        self.gagnant = False
        self.perdant = False
        self.nb_gain = 0
        self.nb_perte = 0