import socket

HOST = 'localhost'
PORT = 5566
BUFF_SIZE = 2048

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mySocket.connect((HOST, PORT))
    print("Client connecter")
    data = "Bonjour chers server!".encode("utf8")
    mySocket.sendall(data) 
except ConnectionRefusedError:
    print("Connexion au server echoue")
finally:
    mySocket.close()
