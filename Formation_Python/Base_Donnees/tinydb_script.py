import os
from tinydb import TinyDB, Query, where
from tinydb.utils import with_typehint

db = TinyDB("data.json", indent=4)
"""
#db.insert({"nom": "Steve", "score": 90}) # insertion simple
db.insert_multiple([
    {"name": "Julie", "score":80},
    {"nom": "Hugo", "score": 70},
    {"nom": "Madara", "score": 100}
]) # insertion multiple
"""
query = Query()
user = db.search(query.name == "Steve") # permet de chercher ce nom dans la base de donnee
user_unique = db.get(query.name == "Steve")

high_score = db.search(where("score") > 0) # avoir les score les score superieur a 0
db.contains(query.name == "Steve") # Permet de savoir si ce nom fait partir de la BD

#db.update({"score": 200}, where("nom") == "Steve") # mettre a jour la table avec cette modification
#db.update({"role": ["pythonista", "javaista"]}, where("nom") == "Steve")
#db.upsert({"nom": "Pierre", "score": 0, "role": ["senior"]}, where("nom") == "Pierre") # ajout nouvelle element
#db.remove(where("score") == 0) # supprime les elements dans la DB
#db.truncate() # supprime tout dans la BD

     
