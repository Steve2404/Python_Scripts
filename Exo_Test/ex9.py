# Programme qui additionne les multiples de 3 et 5 compris de 0 a 32

listM3_5= []  # creation d une liste contenant des multiple de 3 et 5
a= 0        # valeur initiale
som= 0      # notre somme des valeurs

while a<=100 :
    if (not a%3) & (not a%5): # si a%3 == 0 et a%5 == 0 alors,
        var= a                # recuperation de la valeur
        listM3_5.append(var)  # ajout a notre liste
    a= a+1                    # on avance a la valeur suivante
print("les multiples de 3 et 5 sont : ")   
print(listM3_5)
i= 0                          # indice d iteration
while i<len(listM3_5) :  
    som= listM3_5[i] + som    # on fait la somme propement dite
    i= i + 1                  # incrementation de l indice
print("La somme obtenu est de",som,end=' ')#

   
