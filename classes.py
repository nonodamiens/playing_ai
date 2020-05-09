"""Les classes de jeu des allumettes"""

class Game:
    """Classe de définition du jeu (nombre d'allumettes...)"""

    def __init(self, nb):
        """Instanciation d'une partie"""
        self.nb_allumette = nb
        if self.nb_allumette <= 0:
            print("partie terminée")

class Gamer:
    """Classe de définition d'un joueur"""

    def __init__(self):
        """Instanciation d'un joueur"""
        self.gagnant = False
        self.perdant = False
        self.nb_gain = 0
        slef.nb_perte = 0