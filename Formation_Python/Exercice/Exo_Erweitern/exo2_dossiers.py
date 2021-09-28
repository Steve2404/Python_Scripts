from pathlib import Path


chemin = Path(input("ENTREZ UN CHEMIN DE DOSSIER DANS LEQUEL CRÉER LA STRUCTURE"))
     
d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
    "Employes": ["Paul",
                 "Pierre",
                 "Marie"],
    "Exercices": ["les_variables",
                  "les_fichiers",
                  "les_boucles"]}
"""
for dirs in d:
    new_chemin = chemin /dirs
    for el in d[dirs]:
        new_chemin2 = new_chemin / el
        new_chemin2.mkdir(parents= True, exist_ok= True)
"""
## Une autre facon de le faire a l aide de item():
for dossier_principal, sous_dossier in d.items():
    for dossiers in sous_dossier:
        new_chemin = chemin / dossier_principal/dossiers
        new_chemin.mkdir(exist_ok= True, parents= True)  
    