import socket
s = socket.socket()
host = socket.gethostname()
port = 9998
s.bind((host,port))
print "Waiting for connection..."

s.listen(5)
while True:
          conn,addr=s.accept()
          print 'get connection from',addr
          conn.send("server saying hi by aditya")
          conn.close()
