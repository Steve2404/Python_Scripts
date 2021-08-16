def afficher_flottant(flottant):

    if type(flottant) is not float: #Tester si c est un nombre decimal
        raise TypeError("Vous devez entrer un nombre decimal")
    flottant = str(flottant) # convertis en chaine de caractere pour appliquer la methode split
    partie_entier, partie_decimal = flottant.split(".")
    return ",".join([partie_entier, partie_decimal[:3]])

print(afficher_flottant(23.34444444444444444444444))