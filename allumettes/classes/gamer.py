import random

class Gamer:
    """Classe de définition d'un joueur"""

    def __init__(self, human):
        """Instanciation d'un joueur"""
        self.human = human
        self.partie_mem = []
        self.etats = {}
        self.resultat = 0
        self.nb_gain = 0
        self.nb_perte = 0
        self.lr = 0.1

    def reset(self):
        """Remise à zéro des stats du joueur"""
        self.partie_mem = []
    
    def action(self, max = 3, greedy = 0.99, state = [0, 0, 0]):
        """Choix du nombre d'allumette à prendre - choix du joueur humain ou non"""
        if self.human:
            # print("Choix du nombre d'allumettes (max : ", max, "):")
            choix = input('>')
            return choix
        else:
            if random.uniform(0,1) < greedy:
                choix = str(random.randint(1,max))
                # print('choix random :', choix)
            else:
                # print('liste des choix :', state[::-1])
                choix = state[::-1].index(min(state[::-1])) + 1
                # print('choix :', choix)
            return choix

    def partie(self, coup):
        """Memorisation des coups joués"""
        self.partie_mem.append(coup)

    def value_fonction(self, etats, resultat):
        """Calcul de la value fonction"""
        if etats[-1] not in self.etats:
            self.etats[etats[-1]] = self.lr * resultat
        else:
            self.etats[etats[-1]] = self.etats[etats[-1]] + self.lr * (resultat - self.etats[etats[-1]])
        for i in range(len(etats) - 1):
            if etats[-2 - i] not in self.etats:
                self.etats[etats[-2 -i]] = self.lr * self.etats[etats[-1 -i]]
            else:
                self.etats[etats[-2 -i]] = self.etats[etats[-2 -i]] + self.lr * (self.etats[etats[-1 -i]] - self.etats[etats[-2 -i]])

    def winrate(self):
        ''' Calcul du winrate du joueur '''
        return self.nb_gain / (self.nb_gain + self.nb_perte)