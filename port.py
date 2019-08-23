import socket

for i in range (1,65535):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   result = sock.connect_ex(('30.12.44.123',i))
   if result == 0:
      print (i,'Port is open')
   else:
      print ('Port is not open')
      sock.close()
