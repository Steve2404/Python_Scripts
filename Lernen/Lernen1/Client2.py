# Definition d un Client reseau dialoguant avec un serveur

import socket, sys

HOST = 'localhost'#"141.45.180.80"
PORT = 5566

# creation du socket
the_Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Envois d une connexion de socket au serveur
try:
    the_Sock.connect((HOST, PORT))
except socket.error:
    print("Impossible de se connecter a ce serveur !!!")
    sys.exit()

print("La connexion etablie avec le serveur ......")

# Dialogue avec le serveur
msg_Server = the_Sock.recv(1024).decode("utf8")

while 1:
    if msg_Server.upper() == "FIN" or msg_Server == "  " :
        break
    print("S>", msg_Server)
    msg_Client = input("C>")
    the_Sock.sendall(msg_Client.encode("utf8"))
    msg_Server = the_Sock.recv(1024).decode("utf8")

# Fermeture du socket :
print("La connexion interrompue !!!")
the_Sock.close()



