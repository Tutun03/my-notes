import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",9090))
s.listen()
print("listening..")
(c,cip)=s.accept()
otp=input("enter otp")
c.send(otp.encode())
otp=c.recv(1024).decode()
if otp=="8824":
    c.send("you are authenticated".encode())
    data=c.recv(1024).decode()
    print("client says:",data)
    data1= input("Enter Text: ")
    c.send(data1.encode())
else:
    c.send("you are not authenticated".encode())
s.close()
