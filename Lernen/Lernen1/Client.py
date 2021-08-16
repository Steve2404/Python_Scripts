# Definition d un client reseau rudimentaire
# Ce client dialogue avec un server ad hoc

import socket, sys

HOST = 'localhost'
PORT = 5566

# 1. Creation du socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Envois d une requete de connexion au server:
try:
    mySocket.connect((HOST, PORT))
except socket.error :
    print("La connexion au server a echoue.")
    sys.exit()
print("La connexion etablie avec le server.")

# 3. Dialogue avec le server:
msgServer = mySocket.recv(1024).decode("utf8")

while 1:
    if msgServer.upper() == "FIN" or msgServer == " ":
        break
    print("S>", msgServer)
    msgClient = input("C>")
    mySocket.sendall(msgClient.encode("utf8"))
    msgServer = mySocket.recv(1024).decode("utf8")

# 4. Fermeture de la connexion:
print("Connexion interrompue !!!")
mySocket.close()