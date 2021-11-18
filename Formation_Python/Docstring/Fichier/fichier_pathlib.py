import shutil
from os import path
from pathlib import Path

#p = Path("C:/Users/Steve/Documents/Formation_Python")
#print(p.parent)
#print(p.home())
#print(Path.home()) # retourne le dossier utilisateur
#print(Path.cwd()) # retourne le dossier actuelle/ dossier de travaille
#print(dir(p)) # retourner toutes les methodes applicable a la classe Path

#p = Path.home()
#dossiers = ['projet', 'django', 'blog']
#p = p / "Django" # faire la concatenation des chemins
#p = p.joinpath(*dossiers) # joindre les chemin lorsqu on utilise une liste
#p.mkdir(exist_ok=True, parents= True) #pour creer un fichier
#p.rmdir() # suprime un dossier vide
#shutil.rmtree(p)#suprime un dossier non vide


## Creer , Lire dans un fichier

#fichier = Path("C:/Users/Steve/projet/django/index.html")
#fichier.touch() # Cree un nouveau fichier
#fichier.unlink() # Suprime un fichier

#fichier.write_text("Je fais les tests") # ecrire dans un fichier
""" Une autre facon d ecrie dans un fichier
with open(fichier, 'w') as f:
    f.write("Deuxieme facon d ecrie dans un fichier")
"""
#fichier.read_text() # Lire dans un fichier

"""Scanner les fichire dans un dossier: iterdir()
for f in Path.home().iterdir():
    print(f.name ) # donne le nom des fichiers ou dossier 
"""

"""
Scanner les dossier avec plus de flexibilite: glob()
 Pour scanner les dossiers de maniere recurcive: rglob() 
p = Path.home() / "Pictures"
print(p)
for f in p.glob("*.png"):
    print(f.name)
"""


#Cree les constantes d un dossier et  file avec pathlib
#SOURCE_FILE = Path(__file__).resolve() # Permet de resoudre les liens symboliques
#SOURCE_DIR = SOURCE_FILE.parent
#ROOT_DIR = SOURCE_DIR.parent
#DATA_DIR = SOURCE_DIR / "DATA"
#print(SOURCE_FILE)

"""
#Cree les constantes d un dossier et  file avec os

SOURCE_FILE = os.path.realpath(__file__)
#SOURCE_FILE2 = os.path.abspath(__file__)
SOURCE_DIR = os.path.dirname(SOURCE_FILE)
ROOT_DIR = os.path.dirname(SOURCE_DIR)
DATA_DIR = os.path.join(SOURCE_DIR, "DATA")
os.mkdir(DATA_DIR)
print(DATA_DIR)
"""

"""obtenir un chemin entre par l utilisateur
import sys
print(sys.argv[-1])
"""
#
#dossier_utilisateur = Path.home() # C:\Users\Steve
#dossier_courant = Path.cwd() # C:\Users\Steve\Documents\Python Scripts
#
#for f in dossier_courant.iterdir():
#    print(f.name)
#
#print("**1",dossier_utilisateur)
#print("**2",dossier_courant) 
