from threading import Thread
import time

class MonThread(Thread):
    def __init__(self, jusqua):  # jusqu a = valeur supplementaire
        Thread.__init__(self)    # Appel du constructeur de la classe mere
        self.jusqua = jusqua
        self.etat = False   # etat du thread


    def run(self):
        self.etat = True    # on passe en mode marche
        for i in range(0, self.jusqua):
            print("Thread iteration", i)
            time.sleep(2)       #temporise 
        self.etat = False   # on revient en mode arret


m = MonThread(10)   # creation de Thread
m.start()           # lancement du Thread

print("Debut")

while m.etat == False:
    # on attend que le Thread demarre
    time.sleep(2)

while m.etat == True:
    # on attend que le Thread s arrete
    time.sleep(2)

print("Fin")