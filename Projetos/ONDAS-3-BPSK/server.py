# Camada Fisica da Computacao
# Exemplo socket server 
## https://pymotw.com/3/socket/tcp.html

import socket
import sys

class Server():

	def __init__(self):
		self.PORTA = 1234
    	# Create a TCP/IP socket

	def connectSocket(self):
	    
	    print("Initializing socket TCP/IP")
	    # Bind the socket to the port
	    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	    self.server_address = ('localhost', self.PORTA)
	    print("PORTA {}".format(self.PORTA))
	    self.sock.bind(self.server_address)

	    # Listen for incoming connections
	    self.sock.listen(1)

	    while True:
	        # Wait for a connection
			print("Waiting for a connection")
			self.connection, self.client_address = self.sock.accept()
			print(" connection from {}".format(self.client_address))
			break
	
	def receberTexto(self):
        # Receive the data in small chunks and retransmit it
		while True:
			data = self.connection.recv(16)
			print("{}".format(data))
			if len(data) > 0:
				return data
			if(len(data) <= 0):
			    break

	def finishConnection(self):
	# Clean up the connection
		self.connection.close()
