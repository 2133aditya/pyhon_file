import socket
host = socket.gethostname()
port = 12345
s = socket.socket()		# TCP socket object

s.connect((host,port))

s.sendall('This will be sent to server')    # Send This message to server

data = s.recv(1024)	    # Now, receive the echoed
					    # data from server

print data				# Print received(echoed) data
s.close()		
