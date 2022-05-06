class Carte:
    def __init__(self, mana, nom, description):
        self.mana = mana
        self.nom = nom
        self.description = description

    def utiliser(self, entite):
        print(self.description)
