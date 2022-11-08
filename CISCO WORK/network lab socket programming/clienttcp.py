import socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(("127.0.0.1",1234))
while True:
    data=input("enter the  msg")
    c.send(data.encode())
    data=c.recv(1024).decode()
    print("server :",data)
    
