import socket

HOST = ''
PORT = 5566
BUFF_SIZE = 2048

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind((HOST,PORT))
    print("Le server est demmarre ....")
except ConnectionRefusedError:
    print("Impossible de se connecter !")

while 1:
    mySocket.listen(5)
    conn, adress = mySocket.accept()
    print("Un client vient de se connecter ....")

    data = conn.recv(1024)
    data = data.decode("utf8")
    print(data)

conn.close()
mySocket.close()
