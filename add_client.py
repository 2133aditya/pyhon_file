import socket

host = socket.gethostname()
port = 12345
s = socket.socket()

a = str(raw_input('Enter first number: '))	# Enter the numbers
b = str(raw_input('Enter second number: '))	# to be added
c = a+','+b					# Generate a string from numbers

print "Sending string {0} to server" .format(c)


s.connect((host,port))

s.sendall(c)				# Send string 'c' to server
data = s.recv(1024)			# receive server response
print int(data)				# convert received dat to 'int'

s.close()		
