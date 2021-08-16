from threading import Thread, Lock, Event
from time import sleep
import random

lock = Lock()
producer_event = Event() #Benachrichtigung vom Producer an den Consumer
auftrag = [] # Gemeinsamer Puffer

def consumer():
    global auftrag
    while True:
        producer_event.clear() #Event wird gelöscht
        lock.acquire()
        if len(auftrag) == 0 : 
           print("Stopp des Verbrauchs")
           producer_event.set()  #Benachrichtigung vom Consumer an den producer
           producer_event.wait()
           t = random.uniform(1,6)
           sleep(t)
        else:
            job = auftrag.pop(0) # get first element from list
            print("... bearbeite Auftrag #%s" % job)
       
        lock.release()


job_nr = 1 #Aktueller Job
thread = Thread(target = consumer)
thread.start()
while True:
    lock.acquire()
    if len(auftrag) == 10:
        print("Stopp der Produktion")
        producer_event.set()
        producer_event.wait()
        t = random.uniform(1,6)
        sleep(t)
    else:
        auftrag.append(job_nr) #Neues Element produziert
        job_nr = job_nr + 1
        print(auftrag)
    lock.release()

    
   