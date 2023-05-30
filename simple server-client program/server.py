from socket import *
s = socket(AF_INET, SOCK_STREAM)

host = "127.0.0.1"
port = 40674

s.bind((host,port))
print("socket binded to: ", port)

s.listen(5)
print("socket is listening")

while True:
    c, addr = s.accept()
    print("Get connection from ", addr)

    c.send(b'thank you for connection')

    c.close()