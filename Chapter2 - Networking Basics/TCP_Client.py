__author__ = 'Samuel Decanio'

import socket

target_host = "0.0.0.0"
target_port = 9999

#creating a socket object
#AF_INET indicates IPv4 address or hostname
#SOCK_STREAM indicates TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting to client
client.connect((target_host, target_port))

#sending some data
client.send("Sending stuff your way!")

#receive something back (hopefully)
response = client.recv(4096)

print response