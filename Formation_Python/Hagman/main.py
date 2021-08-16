import random
from Hagman_Word import  liste_mot
from Hagman_Art import logo, stages
from replit  import clear


mot_aleatoire = random.choice(liste_mot)
display = []
nbre_vie = len(stages) - 1
game_is_finish = False
print(logo)


#generate many blanks as letter in word
for _ in mot_aleatoire :
    display.append("_")

while not game_is_finish:
    lettre_deviner = input("Entrez une lettre pour deviner le mot : ").lower()
    clear()


    if lettre_deviner in display:
        print(f"Cette lettre: {lettre_deviner},  a deja ete ajoutee ")

    longueur_mot = len(mot_aleatoire)
    for position in range(longueur_mot):
        if mot_aleatoire[position] == lettre_deviner:
            display[position] = lettre_deviner
    print(f"{' '.join(display)}")

    if not lettre_deviner in mot_aleatoire:
        print(f"Cette lettre {lettre_deviner} ne se trouve pas dans le mot . Vous perdez donc une vie ")
        nbre_vie -= 1
        if nbre_vie == 0:
            game_is_finish = True
            print("Game over, vous venez de perdre la partie.")

    if not '_'  in display:
        game_is_finish = True
        print("Vous avez gagnez !")

    print(stages[nbre_vie])



