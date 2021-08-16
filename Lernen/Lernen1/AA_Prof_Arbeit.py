# Bearbeiter 1

import socket
import struct

server_ip = "141.45.180.80" #localhost
server_port = 39998

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# sockets use memory buffers (strings, or bytes)
# multi-byte variables need to be serialized
var = 4 # an integer!
buf = struct.pack("!i8s138s", var, b"test", b"")
# send the packet
client_socket.sendto(buf,(server_ip,server_port))
print ("[*] Message sent.")

# print out what the server sends
response,address = client_socket.recvfrom(1024)
print(address[0])
print ("[*] From: %s Received: %s" % (address[0], response.decode('utf-8')))

client_socket.close()




# Bearbeiter Scheffler
# Beispiel-Code für UDP-Server hinter NAT

import socket
import struct
import sys
from threading import Thread
from time import sleep

server_port = 39998 # Port für die Server-Kommunikation

### Code der als separater Thread ausgeführt wird und die UDP-'Verbindung' offen hält
class Hole_Punch_Thread(Thread):
    def __init__(self,s_socket):
        super(Hole_Punch_Thread, self).__init__()
        #Thread.__init__(self)
        self.s_socket = s_socket
        
    def run(self):

        global server_port    
        buff = b''
        while True:
            self.s_socket.sendto(buff,('141.45.180.80',server_port)) #liam.ipv6lab.f1.htw-berlin.de
            sleep(5) # sendet alle 5 Sekunden ein UDP-Paket, kann angepasst werden


##### Hier kommt ihr normaler Code hin für das Erzeugen und Binden eines Sockets


try:               # Datagram (UDP) socket
   server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   # Die folgende Socket-Option erlaubt es einen Server-Socket schnell erneut zu öffnen 
   server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
   print ('Socket created')
except socket.error as msg:
   print ('Create socket error: ' + str(msg[0]) + ' Message ' + msg[1])
   sys.exit()

try:               # Bind socket to local host and port
   server.bind((socket.gethostname(),server_port))
   print (socket.gethostname())
except socket.error as msg:
   print ('Bind error: ' + str(msg[0]) + ' Message ' + msg[1])
   sys.exit()


#UDP-Hole Punch
newthread = Hole_Punch_Thread(server) 
newthread.start()


# while True:
   ### Hier muss die Nachricht empfangen und dargestellt werden!


server.close()


