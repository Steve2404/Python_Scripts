class Personne:
    """ Classe definissant une personne  caracterise par:
    - son nom
    - son prenom
    - son age
    - son adresse
    """

    def __init__(self, nom, prenom): #  Notre methode constructeur
        """pour l instant on va defini qu un seul attribut"""
        self.nom = nom
        self.prenom = prenom
        self.age = 28
        self.adress = "Berlin"

berna = Personne("Jatsa", "Leonel")
print(berna.nom)