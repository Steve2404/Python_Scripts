##########################################################
# Programme: Realisation d un Jeux de roulette de casino #
# Auteur   : Leonel                                      #
##########################################################

#####################################################
#        Importation des Fonctions Externes:        #
#####################################################
import os
import math
import random

####################################################
#           Definition de la fonction locale       #
####################################################

def parite(nbre):
    if(nbre % 2 == 0):
        val_bool = True
    else:
        val_bool = False
    return val_bool

#######################################################
#                 Corp Principale                     #
#######################################################

print("""
##########################################################
# Programme: Realisation d un Jeux de roulette de casino #
# Auteur   : Leonel                                      #
##########################################################
""")
argent = 1000 
continue_Partie = True

print("Vous commencez avec ", argent," $")
while continue_Partie:

    num_joueur = -1
    while num_joueur < 0 or num_joueur > 49 :
        num_joueur = input("Choisissez un numero entre 0 - 49 :")

        try:
            num_joueur = int(num_joueur)
        except ValueError:
            print("Vous n avez pas saisi un nombre")
            num_joueur = -1
            continue
        if num_joueur < 0:
            print("Vous avez saisi un nombre négatif")
        if num_joueur > 49:
            print("Vous avez saisi un nombre tres grand")

    montant_mise = 0
    while montant_mise <= 0 or montant_mise > argent:
        montant_mise = input("Quel montant aimeriez vous miser ?: ")
        try:
            montant_mise = int(montant_mise)
        except ValueError:
            print("Vous n avez pas saisi un nombre ")
            montant_mise = -1
            continue
        if montant_mise <= 0:
            print("Vous avez saisi un nombre négatif ou null")
        if montant_mise > argent:
            print("Vous n avez que ", argent," $")
        
    somme_retour = 0
    print("\n")
    nbre_aleatoire = random.randrange(50) 
    print("La roulette tourne.......... Et s arrete sur le numero ", nbre_aleatoire)
    if( nbre_aleatoire == num_joueur):
        somme_retour = montant_mise*3
        print("Felicitation!!! vous avez Obtenu ", somme_retour," $\n")
        argent += somme_retour
    elif(parite(nbre_aleatoire) == parite(num_joueur)):
        somme_retour = math.ceil((50*montant_mise)/100)
        print("Vous avez mise sur la bonne couleur. Vous Obtenez ", somme_retour," $\n")
        argent += somme_retour
    else:
        print("Vous avez perdu \n")
        argent -= montant_mise
    
    if argent <= 0:
        print("Vous etes Ruine!!! C est la fin de la Partie")
        continue_Partie = False
    else:
        print("Vous avez a present ", argent," $")
        quitter = input("Souhaitez vous quitter le casino (o/n) ?")
        if quitter == "o" or quitter == "O":
            print("Vous quittez donc le casino avec ", argent," $")
            continue_Partie = False
    
    os.system("pause") 


