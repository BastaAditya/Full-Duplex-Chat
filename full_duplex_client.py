from socket import*
import threading
import getpass

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
print('You are connected to the server.Start your conversattion.')

def receive():
    global tcpCliSock
    while True:
        mssg_s = tcpCliSock.recv(BUFSIZ)
        print("Server : ",end="")
        print(mssg_s.decode('utf-8'))
        if mssg_s.decode('utf-8') == "Bye":
            break

def send():
    global tcpCliSock
    while True:
        mssg_c = getpass.getpass("")
        print("You : ",mssg_c)
        tcpCliSock.send(mssg_c.encode())
        if mssg_c == "Bye":
            break
        
while True:
    t1 = threading.Thread(target = send)
    t2 = threading.Thread(target = receive)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    break
    
tcpCliSock.close()
