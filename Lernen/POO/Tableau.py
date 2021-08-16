class Tableau:
    """Class definissant une surfce sur lequel on peut ecrire et effacer par
    jeux des methodes"""

    def __init__(self):
        self.surface = ""

    def ecrire(self, texte):
        """Methode permettant d ecrire sur la surfce.
        Si la surface n est pas vide on saute une ligne avant d ecrire"""
        if texte != "":
            texte += "\n"
        self.surface += texte

    def lire(self):
        """Cette Methode est chargee d afficher le contenu de notre tableau"""
        print(self.surface)
        
    def effacer(self):
        """Cette Methode efface notre Tableau"""
        self.surface =""

liste = ["Bonjour", "Mango", "Apfel", "Tomate"]
tab = Tableau()
print(tab.surface)
for va in liste:
    tab.ecrire(va)
    tab.lire()
print("Le tableau a ete efface ....")
tab.effacer()
tab.lire()