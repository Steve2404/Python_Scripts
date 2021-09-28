from random import randint

def attaquer(attaque_allie, vie_enemi):
    if vie_enemi > 0:
        vie_enemi -= attaque_allie
        return vie_enemi
    else:
        return 0
def potion(vie_user, qte_potion):
    vie_user += qte_potion
    return vie_user


print("Bienvenue a ce RPG")
point_vie_user = point_vie_cpu = 50
nbre_potion = 3
choix = ""
skip_turn = False

while True:
    if skip_turn:
        print("Vous passez le tour ........")
        skip_turn = False
    else:
        choix = ""
        while not (choix.isdigit() and (choix == "1" or choix == "2")):
            choix = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?")
        attaque_user = randint(5, 10)  
        attaque_cpu = randint(5, 15)
        if int(choix) == 1:
            point_vie_cpu = attaquer(attaque_user, point_vie_cpu)
            print(f"Vous avez inflige {attaque_user} point de vie a votre adversaire")
            print(f"    Il vous reste {point_vie_user} points et votre adversaire {point_vie_cpu} point ")
            if point_vie_cpu <= 0:
                break
        else:
            if nbre_potion > 0:
                potion_vie = randint(15, 50)
                point_vie_user = potion(point_vie_user, potion_vie)
                nbre_potion -= 1
                skip_turn = True
                print(f"Activation de la potion de vie ❤, vous gagnez {potion_vie} point de vie")
            else:
                print("Vous n avez plus assez de potion.")
                continue

    print("C'est au tour de votre adversaire d'attaquer.")
    point_vie_user = attaquer(attaque_cpu, point_vie_user)
    print(f"Votre adversaire vous a inflige {attaque_cpu} point de vie ") 
    print(f"    Il vous reste {point_vie_user} points et votre adversaire {point_vie_cpu} point ")

    if point_vie_user <= 0:
        break
    print("-"*70)

if point_vie_user > point_vie_cpu:
    print(f"Felicitation 👏👏 Vous avez gagnez avec {point_vie_user} retant.")
elif point_vie_user < point_vie_cpu:
    print(f"😔😔 Desole vous avez perdu 🥺🥺 et votre adversaire a {point_vie_cpu} restant")
else:
    print("C'est un match nul 🤝🤝")

