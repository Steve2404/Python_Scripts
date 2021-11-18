from pprint import pprint
chemin = r"C:\Users\Steve\Documents\Python Scripts\Formation_Python\Exercice\exo3_fichiers\prenoms.txt"

with open(chemin, "r") as f:
    contenu = f.read().splitlines()
    
    
prenons = []
for line in contenu:
    prenons.extend(line.split()) 
liste_prenoms = [pr.strip(",. ") for pr in prenons]
liste_prenoms.sort()
with open(chemin, "w") as f:
    f.write("\n".join(liste_prenoms))
