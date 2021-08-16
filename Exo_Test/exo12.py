# Programme de saisir des notes, affiche la moyenne, la note Max et Min
#Prend fin si le user entre un valeur negative

note= 0
liste_note= []
note_max= 0
note_min= 20
moyen= 0
nbre_note= 0
som= 0

# Rempli notre liste avec les notes
while(note>=0) :
    note= int(input("Entrez une note positive de 0 a 20 : "))# demande d une note
    if note<0 : 
         print("Termine") # arret si la note est negative
         
    else:
        liste_note.append(note) # mise a jour de note liste

if not liste_note: # cas ou la liste est vide
    print("Impossible d effectuer des calculs sur un tableau vide ")
else:

    # Calcule la note maximale et minimale
    nbre_note= len(liste_note)
    i= 0
    while i<nbre_note :        # on ne doit pas depasser le nbre de note

        if(liste_note[i]>note_max) :
            note_max= liste_note[i]   # on trouve la note maximale
        if(liste_note[i]<note_min) :
            note_min= liste_note[i]   # on trouve la note minimale
        i= i+1

    # Calcul de la moyenne
    j= 0
    while j<nbre_note :
        som= som + liste_note[j] # Calcul la somme total des notes
        moyen= som/nbre_note   # Calcul de la moyenne
        j= j+1

    #Affichage du resultat
    print(note_min," est la note minimale et ",note_max," est la note maximale ",end="\n")
    print(moyen, " est la moyenne des ", nbre_note," notes", end=" ")
   
    