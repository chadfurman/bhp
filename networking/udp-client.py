import socket

target_host = "localhost"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# connect the client
client.sendto("AAABBBCCC",(target_host,target_port))

# receive some data
data, addr = client.recvfrom(4096)

print response
