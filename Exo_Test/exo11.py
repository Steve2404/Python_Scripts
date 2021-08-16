# Programme qui affiche le nom d une personne y compris son sexe

List_nom= [] # Creation d une liste de nom
nom= input("Entrez un nom svp: ") # Saisir un nom
List_nom.append(nom)                  # l introduit a l emplacement 0 de la liste
sexe= input("Entrez un sexe (M/F): ") # Le type de sexe
List_nom.append(sexe)                 # ajoute a notre liste
if List_nom[1] == "M" :               # si l attribut est masculin, alors
    attri= "Monsieur"
    ch= "Cher"
elif List_nom[1] == "F" :             # Sinon l attribut est fiminin, alors
    attri= "Madame"
    ch= "Chere"
else:                                 # aucun des cas
    attri=" "
    ch= " "

print(ch, attri, List_nom[0], end=" ")