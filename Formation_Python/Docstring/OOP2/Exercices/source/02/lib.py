import logging
import os, json

from constant import DATA_DIR

LOGGER = logging.getLogger() # permet d afficher les resultats en fonction du levelname


class Liste(list):

    def __init__(self, nom):
        self.nom = nom

    def ajouter(self, element):
        if not isinstance(element, str): # On verifie si l element est une instance de la classe str
            raise ValueError("Vous ne pouvez que des chaines de caracteres !")
        if element in self:
            LOGGER.error(f"{element} est deja dans la liste.")
            return False
        self.append(element)
        LOGGER.info(f"{element} a ete bien ajoute a la kiste")
        return True
    
    def enlever(self, element):
        if element in self:
            self.remove(element)
            LOGGER.info(f"{element} a ete bien retire")
            return True
        return False

    def afficher(self):
        print(f"*** Ma liste de {self.nom} ***")
        for element in self:
            print(f"- {element}")
    
    def sauvegarder(self):
        chemin = os.path.join(DATA_DIR, f"{self.nom}.json")
        try:
           if not os.path.exists(DATA_DIR): 
                os.makedirs(DATA_DIR)
        except FileExistsError:
            print("Ce dossier existe deja")
            return False

        with open(chemin, "w") as f:
            json.dump(self, f, indent= 3)
        return True
        



if __name__ == "__main__":
    liste = Liste("course")
    liste.ajouter("mangue")
    liste.ajouter("riz")
    liste.ajouter("Banane")
    liste.ajouter("Mais")
    liste.afficher()
    liste.sauvegarder()
    liste2 = Liste("Travaux")
    liste2.ajouter("puiser de l eau")
    liste2.ajouter("laver les habits")
    liste2.afficher()
    liste2.sauvegarder()
