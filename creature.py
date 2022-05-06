from carte import Carte

class Creature(Carte):
    def __init__(self, mana, nom, description, pv, atk):
        Carte.__init__(self, mana, nom, description)
        self.pv = pv
        self.atk = atk