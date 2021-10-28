class Voiture:

    def __init__(self, essence = 100) -> None:
        self.essence = essence
    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence} litres d’essence")
    
    def roule(self, km):
        litre_consum = (5*km)/100
        if self.essence <= 0:
            print(" Vous n'avez plus d'essence, faites le plein !")
            return
        elif self.essence < 10:
            print("Vous n'avez bientôt plus d'essence !")
        else:
            self.essence -= litre_consum
        self.afficher_reservoir()

    def faire_le_plein(self):
        self.essence = 100
        print("Vous pouvez repartir !")


voiture01 = Voiture()
voiture02 = Voiture()
voiture01.afficher_reservoir()
voiture02.roule(50)
voiture02.afficher_reservoir()
voiture01.roule(1000)
voiture02.roule(100)
voiture01.afficher_reservoir()
voiture02.afficher_reservoir()
    