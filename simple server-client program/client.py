from socket import *
s = socket(AF_INET, SOCK_STREAM)

host = "127.0.0.1"
port = 40674

s.connect((host,port))

print(s.recv(2048))

s.close()
