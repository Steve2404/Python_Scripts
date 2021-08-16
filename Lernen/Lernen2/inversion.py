def afficher(*parametre, sep=' ', end='\n'):
    parametre = list(parametre)  # conversion du tuple en liste
    chaine = ' '

    for i, chaine in enumerate(parametre):
        parametre[i] = str(chaine)

    chaines = sep.join(chaine)
    chaines += end

    print(chaines, end=' ')


ch = "Bien le bonjour chers tous die jungen Mädchen"
afficher(ch)