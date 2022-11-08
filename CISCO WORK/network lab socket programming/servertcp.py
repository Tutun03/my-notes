import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",1234))
s.listen()
print("server is listening")
while True:
    (c,cip)=s.accept()
    data=c.recv(1024).decode()
    print("data is received",data)
    data=input("enter the text :")
    c.send(data.encode())
