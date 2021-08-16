def Affich_flottant(flottant) :

    if type(flottant) is not float :
        raise TypeError("Le parametre doit etre un flottan")
    flottant= str(flottant)
    partie_entier, partie_decimal= flottant.split(".")
    return ",".join([partie_entier, partie_decimal[:3]])
    print("Erreur")
