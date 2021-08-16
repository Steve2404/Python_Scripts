import socket
import struct
import sys
from threading import Event, Thread
from time import sleep

server_port   = 39998 # Arbitrary non-privileged port
server_adress = 'localhost'
class Hole_Punch_Thread(Thread):
    def __init__(self,s_socket):
        super(Hole_Punch_Thread, self).__init__()
        #Thread.__init__(self)
        self.s_socket = s_socket
        
    def run(self):

        global server_port    
        buff = b''
        while True:
            self.s_socket.sendto(buff,('141.45.180.80',39998)) #liam.ipv6lab.f1.htw-berlin.de (141.45.180.80)
            sleep(5)



try:               # Datagram (UDP) socket
   server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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


print ("[*] UDP_Server started on %s:%s" % server.getsockname())
while True:        # receive data from client (data, addr)
   data, addr = server.recvfrom(1024)
   
   print ("[*] Received data from: %s:%d" % (addr[0],addr[1]))
   a,b,c = struct.unpack('!i8s138s',data)
   print ("[*] User: %s - %s" % (b.decode("utf-8"),c.decode("utf-8")))


server.close()
