
def Eratosthenes(N):
    liste_nbre_premier = [1]
    for n in range(N):
       cmpP = 1
       if n > 1:
           for i in range(2, n):
               if n % i == 0:
                   cmpP += 1
           if cmpP < 2:
               liste_nbre_premier.append(n)
    print(liste_nbre_premier)
Eratosthenes(100)

def Eratosthenes2(N):
    liste = []
    for el in range(1, N):
        liste.append(el)

    for i in range(1, len(liste)):
        for j in range(i+1, len(liste)):
            c =  liste[i]*j
            if c in liste:
                liste.remove(c)
    print(liste)
Eratosthenes2(100)




