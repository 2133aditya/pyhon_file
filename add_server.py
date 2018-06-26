import socket
host = socket.gethostname()
port = 12345
s = socket.socket()		    # TCP socket object
s.bind((host,port))

s.listen(5)

conn, addr = s.accept()
print "Connected by ", addr
while True:
	data=conn.recv(1024)
	# Split the received string using ','
	# as separator and store in list 'd'
	d = data.split(",")	    
	
	# add the content after converting to 'int'
	data_add = int(d[0]) +int(d[1]) 
	
	conn.sendall(str(data_add))	    # Send added data as string
					                # String conversion is MUST!
conn.close()
