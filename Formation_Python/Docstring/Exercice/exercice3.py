"""Liste des course"""
import sys

liste_element = []
while True:
    liste_action = ["Ajouter", "Retirer", "Afficher", "Vider", "Quitter"]
    print("Choisissez parmir les 5 options.")
    for i, action in enumerate(liste_action):
        print(i+1,":", action)


    choix = int(input("Votre choix :👉"))
    if choix == 1:
        entre1 = input("Entrez le nom de l'element à ajouter dans la liste: ")
        liste_element.append(entre1)
        if entre1 in liste_element:
            print(f"L'élement {entre1} a été bien ajouté dans la liste")
    elif choix == 2:
        entre1 = input("Entrez le nom de l'élément à retirer de la liste: ")
        if entre1 in liste_element:
            liste_element.remove(entre1)
            print(f"L'élément {entre1} a été bien retiré de la liste")
        else:
            print(f"L'élément {entre1} n'est pas dans la liste")

    elif choix == 3:
        if len(liste_element) == 0:
            print("Votre liste est encore vide.")
        else:
            print("Voici le contenu de votre liste: ")
            for i, elem in enumerate(liste_element, 1):
                print(i,".",elem)
    elif choix == 4:
        if len(liste_element) > 0:
            liste_element.clear()
            print("Votre liste a été bien vidée. ")
        else:
            print("Votre liste est deja vide.")
    elif choix == 5:
        print("Aurevoir !!!")
        sys.exit()
    print("-"*50)


