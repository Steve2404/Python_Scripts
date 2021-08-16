# Definition d un serveur reseau rudimentaire
#Ce serveur attend la connexion d un client

import socket, sys

HOST = 'localhost'
PORT = 5566
counter = 0   # compteur de connexion active
server_name = "Leonel" # Nom du server
 
 # 1. Creation du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 # 2. liaison du socket a une adresse precise
try:
    mySocket.bind((HOST, PORT))
except ConnectionRefusedError: 
    print("La liaison du socket a l adresse choisie a echoue.")
    sys.exit
    
while 1:
    # 3. Attente de la requete de connexion d un client
    print("Serveur pret, en attente de requetes......")
    mySocket.listen(2)

    # 4. Etablissement de la connexion:
    connexion, adresse = mySocket.accept()
    counter += 1
    print("Client connecte, adresse IP {0}, port {1} " .format(adresse[0], adresse[1]))

    # 5. Dialogue avec le client :
    msgServeur = ("Vous etes connecte au serveur %s . Envoyez vos messages. " %(server_name))
    connexion.send(msgServeur.encode("Utf8"))
    msgClient = connexion.recv(1024).decode("Utf8")
    while 1:
        print("C>", msgClient)
        if msgClient.upper() == "FIN" or msgClient == " ":
            break
        msgServeur = input("S> ")
        connexion.send(msgServeur.encode("Utf8"))
        msgClient = connexion.recv(1024).decode("Utf8")

    # 6. Fermeture de la connexion :
    connexion.send("fin".encode("Utf8"))
    print("Connexion interrompue.")
    connexion.close()

    ch = input("<R>ecommencer <T>erminer ?")
    if(ch.upper() == 'T'):
        break



