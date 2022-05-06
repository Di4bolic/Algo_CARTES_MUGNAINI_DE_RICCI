from contextlib import nullcontext
from carte import Carte
from mage import Mage
from cristal import Cristal
from creature import Creature
from blast import Blast

# Mise en place

carte1 = Carte(5, "inutile", "Vous voyez un caillou ...\n")
carte2 = Carte(10, "inutile", "Vous voyez un gros caillou !\n")
carte3 = Cristal(0, "cristalDeMana", "Votre mana maximum augmente définitivement de 5 !\n", 5)
carte4 = Creature(15, "creature", "Un gros méchant arrive dans la zone de jeu ! ( 5 pv , 5 atk )\n", 5, 5)
carte5 = Blast(10, "blast", "Vous lancez un sort qui inflige 5 dégâts !\n", 5)

perso1 = Mage("Confucius", 20, 20)

perso1.remplirMain(carte1)
perso1.remplirMain(carte2)
perso1.remplirMain(carte3)
perso1.remplirMain(carte4)
perso1.remplirMain(carte5)

# Création d'un deuxième joueur

perso2 = Mage("Confiture", 20, 20)

perso2.remplirMain(carte1)
perso2.remplirMain(carte2)
perso2.remplirMain(carte3)
perso2.remplirMain(carte4)
perso2.remplirMain(carte5)

print(" ")
perso2.jouerCarte(3, nullcontext)

# Jeu

print("Votre main :\n")
perso1.montreMain()

print(" ")
choix = int(input("Quelle carte voulez-vous jouer ? "))
print(" ")

# Différentes possibilités

if perso1.main[choix].nom == "cristalDeMana":
    perso1.jouerCarte(choix, perso1)
elif perso1.main[choix].nom == "blast":
    print("Zone de jeu adverse :\n")
    perso2.montreZoneDeJeu()
    print("Joueur adverse --> joueur")
    print(" ")
    choixBis = input("Quelle carte/joueur attaquez-vous ? ")
    print(" ")
    if choixBis == "joueur":
        perso1.jouerCarte(choix, perso2)
    else:
        perso1.jouerCarte(choix, perso2.zoneDeJeu[int(choixBis)])
else:
    perso1.jouerCarte(choix, nullcontext)

# Check pour savoir si les creatures adverses sont en vie

for i in range(len(perso2.zoneDeJeu)):
            if perso2.zoneDeJeu[i].nom == "creature" and perso2.zoneDeJeu[i].pv <= 0:
                perso2.defausse.append(perso2.zoneDeJeu[i])
                del perso2.zoneDeJeu[i]
                print("La créature adverse est morte !\n")

# Attaque du joueur

print("Votre zone de jeu :\n")
if perso1.montreZoneDeJeu() != 0:
    print(" ")
    choix = int(input("Avec quelle créature voulez-vous attaquer ? "))
    print(" ")
    print("Zone de jeu adverse :\n")
    perso2.montreZoneDeJeu()
    print("Joueur adverse --> joueur")
    print(" ")
    choixBis = input("Quelle carte/joueur attaquez-vous ? ")
    print(" ")
    if choixBis == "joueur":
        perso2.pv -= perso1.zoneDeJeu[choix].atk
    else:
        perso2.zoneDeJeu[int(choixBis)].pv -= perso1.zoneDeJeu[choix].atk

        # Check pour savoir si les creatures adverses adverses sont en vie

        for i in range(len(perso2.zoneDeJeu)):
            if perso2.zoneDeJeu[i].nom == "creature" and perso2.zoneDeJeu[i].pv <= 0:
                perso2.defausse.append(perso2.zoneDeJeu[i])
                del perso2.zoneDeJeu[i]
                print("La créature adverse est morte !\n")
            else:
                # Contre-attaque
                perso1.zoneDeJeu[choix].pv -= perso2.zoneDeJeu[int(choixBis)].atk
                # Check pour savoir si notre creature est en vie
                if perso1.zoneDeJeu[choix].pv <= 0:
                    perso1.defausse.append(perso1.zoneDeJeu[choix])
                    del perso1.zoneDeJeu[choix]

    # Check pour savoir si le joueur adverse est en vie

    if perso2.pv <= 0:
        print("Victoire pour " + perso1.nom + " !\n")

else:
    print("Votre zone de jeu est vide\n")