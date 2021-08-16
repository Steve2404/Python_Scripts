from threading import Thread
import time
import threading

class MonThread(Thread):
    def __init__(self, jusqua, event):  # jusqu a = valeur supplementaire
        Thread.__init__(self)    # Appel du constructeur de la classe mere
        self.jusqua = jusqua
        self.event = event       #garde un acces a l objet event


    def run(self):
        for i in range(0, self.jusqua):
            print("Thread iteration", i)
            time.sleep(2)       #temporise 
        self.event.set()        # on indique qu on a fini : On active l objet self.event



print("Debut")
event = threading.Event()      # on cree  un objet de type Event
event.clear()                  # on desactive l objet  Event

m = MonThread(10, event)       # creation de Thread
m.start()                      # lancement du Thread
while not event.is_set():
    print("J attend")
    event.wait()
#event.wait()                   # on attend jusqu a ce que l objet soit active  

print("Fin")