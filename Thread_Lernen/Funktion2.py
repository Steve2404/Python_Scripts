import time
from threading import Thread
"""Definiton von unsere Funktion, die von Thread erbt"""

class Countdown(Thread):
    def __init__(self, n):
        super(Countdown, self).__init__()
        self.n = n

    def run(self):
        while self.n>0 :
            print("T-minus", self.n)
            self.n -= 1
            time.sleep(1)
            print("Engine start")


t = Countdown(10)
t.start()
t.join()
print("Fin du programme!!!")