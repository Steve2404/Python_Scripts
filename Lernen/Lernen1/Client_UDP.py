import socket
import struct

server_ip =  '127.0.0.1' #'141.45.180.80'
server_port = 39998

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

var = 4
username = "Steve"
Msg = "Bonsoir"
buf = struct.pack("!i 8s 138s", var,username.encode('ASCII'), Msg.encode('ASCII'))

# Daten ubertragen
client_socket.sendto(buf, (server_ip, server_port))
print("[*] Message sent.")

# Der Antwort des Servers
response, adresse = client_socket.recvfrom(1024)
print(adresse[0])
print("[*] From: %s  Received: "% (adresse[0], response.decode('utf8')))
client_socket.close()
