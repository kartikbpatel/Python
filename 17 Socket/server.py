# steps are
# 1. create a socket
# 2. bind the socket to an IP address and port
# 3. listen for a connection
# 4. aceept the connection
# 5. receive the request
# 6. send the response

import socket
import sys

# step 1
try:
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print("Failed to create socket")

	# to quit the program
	sys.exit()

# step 2
# first arg (host) is empty, can receive from any host
# second arg (port)
try:
	mysock.bind(("",1234))
except socket.error:
	print("Failed to bind")
	sys.exit()

# step 3
# listen() starts listening for a connect()
# arg is backlog, number of requests allowed (for clients) to wait for service
mysock.listen(5)

# as the server is always live (A Live Server)
while True:
	# step 4
	# accept a connection request
	conn, addr = mysock.accept()
	# step 5
	data = conn.recv(1000)
	if not data:
		break
	# step 6
	conn.sendall(data)

conn.close()
mysock.close()