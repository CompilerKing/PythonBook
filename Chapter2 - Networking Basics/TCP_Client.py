__author__ = 'Samuel Decanio'

import socket

target_host = "www.google.com"
target_port = 80

#creating a socket object
#AF_INET indicates IPv4 address or hostname
#SOCK_STREAM indicates TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting to client
client.connect((target_host, target_port))

#sending some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive something back (hopefully)
response = client.recv(4096)

print response