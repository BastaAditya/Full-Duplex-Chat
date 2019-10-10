from socket import*

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('...waiting for connection')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from',addr)

    while True:

        mssg_c = tcpCliSock.recv(BUFSIZ)
        print("Client : ",end="")
        print(mssg_c.decode('utf-8'))
        if mssg_c.decode('utf-8') == "Bye":
            break
        mssg_s = input('You: ')
        tcpCliSock.send(mssg_s.encode())
        if mssg_s == "Bye":
            break
    tcpCliSock.close()
tcpSerSock.close()
        
        
    
    
