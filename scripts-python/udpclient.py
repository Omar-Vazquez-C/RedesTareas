import socket

print("UDP Client ")

target_host = "127.0.0.1"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
v client.sendto("AAABBBCCC",(target_host,target_port))

# receive some data
w data, addr = client.recvfrom(4096)

print data