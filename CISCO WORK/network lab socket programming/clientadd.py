import socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(("127.0.0.1",9090))
while True:
    a=input("enter the value of a:")
    b=input("enter the value of b:")
    c.send(a.encode())
    c.send(b.encode())
    new=c.recv(1024).decode()
    print("server:",new)
