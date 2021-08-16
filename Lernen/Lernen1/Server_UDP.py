import socket
import struct
import sys

server_ip = '127.0.0.1'
server_port = 9999

#UDP Socket Erstellung
try:
    server_Udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket created")
except socket.error as msg:
    print("Create socket error: "+ str(msg[0]) + " Message " + msg[1])
    sys.exit()

# Verbindung des SOCKETS mit HOST und PORT
try:
    server_Udp.bind((server_ip, server_port))
except socket.error as msg:
    print("Bind error: " + str(msg[0]) + " Message " + msg[1])
    sys.exit()

print("[*] UDP_Server started on %s:%s " %server_Udp.getsockname())
while 1:
    data, adress = server_Udp.recvfrom(1024)
    print("[*] Received data from: %s:%d" %(adress[0], adress[1]))
    server_Udp.sendto(b"Ack - %i" %struct.unpack('!i', data), adress)

server_Udp.close()

