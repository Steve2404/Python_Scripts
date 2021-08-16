# Definition d un serveur qui attend la connexion du client

import socket, sys

HOST = "localhost"
PORT = 5566
server_name = "Leonel"
counter = 0

# Creation du socket:
the_Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du socket a une adresse bien precise:
try:
    the_Sock.bind((HOST, PORT))
except socket.error:
    print("Connexion au niveau du server a echoue.")
    sys.exit()

while 1:
    # Attente de la requete du client
    print("Server connecte , pret a l emploi !!!")
    the_Sock.listen(2)

    # Etablissement de la connexion:
    connex, adress = the_Sock.accept()
    counter += 1
    print("Le Client connecte au serveur {}, avec une @IP: {}; PORT: {}" .format(server_name, adress[0], adress[1]))
    print("Le client s est connecte {} fois" .format(counter))

    # Dialogue avec le Client:
    msg_server = ("Bienvenue dans le server {}" .format(server_name))
    connex.sendall(msg_server.encode("utf8"))
    msg_client = connex.recv(1024).decode("utf8")

    while 1:
        print("C>", msg_client)
        if msg_client.upper() == "FIN" or msg_client == "  " :
            break
        msg_server = input("S>")
        connex.sendall(msg_server.encode("utf8"))
        msg_client = connex.recv(1024).decode("utf8")
    
    # Fermeture de la session
    connex.sendall("fin").encode("utf8")
    print("Connexion interrompue !!!")
    the_Sock.close()
    
    ch = input("<R>ecommencer ou <T>erminer")
    if ch.upper() == "T":
        break
