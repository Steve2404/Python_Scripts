# Programme qui dit si une Annee entree par le user est bissextile

An= int(input("Entrez une Annee svp : "))  # saisir l annee par le user et le convertis en entier

if (((not An%4)or(not An%400)) and (An%100)) :   # si l annee est multiple de 4, 400 et non de 100 alors
    print(An," est une Annee bissextile", end=" ")
else: # si Annee est multiple de 100 et non celui de 400 , alors
    print(An," n est pas une Annee bissextile")







   



