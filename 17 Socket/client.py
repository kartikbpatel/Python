# Steps are 
# 1. create socket at client
# 2. connect socket to server
# 3. send data to server
# 4. wait for response from server
# 5. close the socket at client

# Exceptions are,
# 1. socket.error
# 2. socket.gaierror > getaddressinfo()

import socket
import sys

# step 1
# AF_INET declares address family internet
# SOCK_STREAM indicates TCP (connection-based)
try:
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print("Failed to create socket")

	# to quit the program
	sys.exit()

# step 2
# performs DNS lookup
try:
	host = socket.gethostbyname("www.google.com")
except socket.gaierror:
	print("Failed to get host")
	sys.exit()

mysock.connect((host,80))

# step 3
message  = "GET / HTTP/1.1\r\n\r\n"

try:
	mysock.sendall(message.encode(encoding='utf_8'))
except socket.error:
	print("Failed to send")
	sys.exit()

# step 4
# 1000 is the maximum number of bytes to receive
data = mysock.recv(1000)
print(data)


# step 5
# to free up port
mysock.close()