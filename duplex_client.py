from socket import*

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
print('You are connected to the server.Start your conversattion.')

while True:
    
    print('You: ',end="")
    mssg_c = input()
    tcpCliSock.send(mssg_c.encode())
    if mssg_c == "Bye":
        break
    mssg_s = tcpCliSock.recv(BUFSIZ)
    print("Server: ",end="")
    print(mssg_s.decode('utf-8'))
    if mssg_s.decode('utf-8') == "Bye":
        break

tcpCliSock.close()
    
    
