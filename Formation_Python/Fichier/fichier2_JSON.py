import json

chemin = r"C:\Users\Steve\Documents\Python Scripts\Formation_Python\Fichier\fichier_j.json"

"""pour ecrire dans un fichier json"""
#with open(chemin, "w") as f:
    #json.dump("Bonjour", f) # Ajouter un nouveau element dans le fichier json
    #json.dump(list(range(10)), f, indent= 3) # cree une liste dans notre fichier json

"""pour lire dans un fichier json"""
#with open(chemin, "r") as f:
#    liste = json.load(f) # lire un fichier json
#    print(liste)

"""pour ajoute un element dans un fichier json
1. on lire d abord le fichier
2. on ajoute ensuite l element dans le fichier
3. on reecrit le fichier json"""
with open(chemin, "r") as f: #1. lire le fichier
    donnee = json.load(f)
donnee.append(10)             #2. ajoute l element dans le fichier
with open(chemin, "w") as f: #3. on reecrit le fichier
    json.dump(donnee, f, indent= 3, ensure_ascii= False)