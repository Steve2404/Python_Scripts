chemin = r"C:\Users\Steve\Documents\Python Scripts\Formation_Python\Fichier\fichier_text1.txt" #convertis en Rawstring

"""lire un fichier"""
#with open(chemin, "r") as f: # ouvrir un fichier
    #contenu = f.read()
    #contenu = f.read().splitlines() #transforme en liste
    #print(contenu)

"""écrire dans un fichier"""

with open(chemin, "a") as f: #ajouter un nouveau element dans le fichier
    f.write("\net\nFormidable ")