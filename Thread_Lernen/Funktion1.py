import time
from threading import Thread

def countdown(n):
    while n >0 :
        print('Time-minus', n)
        n -= 1
        time.sleep(3)
    print("Engine Start")

#creation et execution d un Thread
t = Thread(target=countdown, args=(10,))
t1 = Thread(target=countdown, args=(20,))
t.start()
t1.start()
t.join()
#t1.join()
#countdown(10)
#countdown(20)
print("Fin du programme!")