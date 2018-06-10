#socket_echo_client.py
import socket
import sys	

# Create a TCP/IP socket
class Client():

	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = ('localhost', 1235)

	def main(self, message):
		# Connect the socket to the port where the server is listening
		print('connecting to {} port {}'.format(*self.server_address))
		self.sock.connect(self.server_address)

		try:

		    # Send data
		    
		    print('sending {!r}'.format(message))
		    self.sock.sendall(message)

		    # Look for the response
		    # amount_received = 0
		    # amount_expected = len(message)

		    # while amount_received < amount_expected:
		    #     data = sock.recv(16)
		    #     amount_received += len(data)
		    #     print('received {!r}'.format(data))

		finally:
		    print('closing socket')
		    self.sock.close()
