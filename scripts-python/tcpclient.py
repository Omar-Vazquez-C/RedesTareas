import socket

print("TCP Client ")

target_host = "www.google.com"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connec the client
client.connect((target_host,target_port))

# send some data 
# .encode to turn the data into ascii so the code can be read
data = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(data.encode("ascii"))

# receive some data
# we must decode the response by usign .decode method before printing it
response = client.recv(4096)

res = response.decode("ascii")

print (res)