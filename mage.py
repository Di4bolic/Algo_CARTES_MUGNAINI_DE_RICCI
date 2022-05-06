class Mage:
    def __init__(self, nom, pv, manaMax):
        self.nom = nom
        self.pv = pv
        self.manaMax = manaMax
        self.manaActuel = manaMax

        self.main = []
        self.defausse = []
        self.zoneDeJeu = []

    def remplirMain(self, carte):
        self.main.append(carte)

    def montreMain(self):
        # Regen mana
        self.manaActuel += 5
        # montrer les cartes
        for i in range(len(self.main)):
            print(self.main[i].nom + " --> " + str(i))

    def montreZoneDeJeu(self):
        # montrer les cartes creature
        compteur = 0
        for i in range(len(self.zoneDeJeu)):
            if self.zoneDeJeu[i].nom == "creature":
                print(self.zoneDeJeu[i].nom + " --> " + str(i))
                compteur += 1
        return compteur

    def jouerCarte(self, numCarte, entite):
        self.manaActuel -= self.main[numCarte].mana
        if self.main[numCarte].nom == "blast":
            self.defausse.append(self.main[numCarte])
        else:
            self.zoneDeJeu.append(self.main[numCarte])
        self.main[numCarte].utiliser(entite)
        del self.main[numCarte]

    def attaque(self,entite):
        pass