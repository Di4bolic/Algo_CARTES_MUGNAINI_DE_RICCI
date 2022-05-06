from carte import Carte

class Blast(Carte):
    def __init__(self, mana, nom, description, valeur):
        Carte.__init__(self, mana, nom, description)
        self.valeur = valeur

    def utiliser(self, entite):
        print(self.description)
        entite.pv -= self.valeur