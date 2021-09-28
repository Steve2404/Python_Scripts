from pathlib import Path
"""
try:
    chemin = Path(input("Entrez un chemin de fichier: "))
    with open(chemin, "r") as f:
        contenu = f.read()
        print(contenu)
except UnicodeDecodeError:
    print("Ce fichier es invalide")
except FileNotFoundError as e:
    print("Erreur: ", e)
"""

### Autre facon
chemin = Path(input("Entrez un chemin de fichier: "))
try:
    f = open(chemin, "r")
    print(f.read())
except UnicodeDecodeError:
    print("Ce fichier es invalide")
except FileNotFoundError as e:
    print("Ce fichier n existe pas")
else:
    f.close()
