"""Les classes de jeu des allumettes"""

class Game:
    """Classe de définition du jeu (nombre d'allumettes...)"""

    def __init(self, nb):
        """Instanciation d'une partie"""
        self.nb_allumette = nb
        if self.nb_allumette <= 0:
            print("partie terminée")