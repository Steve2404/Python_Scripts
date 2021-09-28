nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombre_paire = [i for i in nombres if i%2 == 0]
print(nombre_paire)

nombre2 = range(10)
nombre_inver = [i if i%2 == 0 else -i for i in nombre2]
print(nombre_inver)

"""Un autre facon de tester la validite de ce que entre le user dans le programe"""
choice = ""
while choice not in ["1", "2"]:
    choice = input("Entrez '1' pour Attaquer et '2' pour defendre")