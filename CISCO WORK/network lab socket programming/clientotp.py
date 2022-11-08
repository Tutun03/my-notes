import socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(("127.0.0.1",9090))
data1=c.recv(1024).decode()
print("server entered otp is:",data1)
otp=input("enter the correct otp")
c.send(otp.encode())
data1=c.recv(1024).decode()
print("confirmation is :" , data1)
if data1=="you are authenticated":
    data1 = input("Enter Text: ")
    c.send(data1.encode())
    data1=c.recv(1024).decode()
    print("server says :",data1)
else:
    c.close()
