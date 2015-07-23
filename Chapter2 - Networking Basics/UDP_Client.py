__author__ = 'SDecanio'

import socket

target_host = "127.0.0.1"
targat_port = 80

#creating a socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#sending data
client.sendto("AAABBBCCC", (target_host, targat_port))

#receive something back
data, addr = client.recvfrom(4096)

print data