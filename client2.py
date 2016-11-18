
import socket   #for sockets
import sys  #for exit

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

print 'Socket Created'

host = '192.168.1.147';
port = 8008;

try:
    remote_ip = socket.gethostbyname( host )

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

#Connect to remote server
s.connect((remote_ip , port))

print 'Socket Connected to ' + host + ' on ip ' + remote_ip
reply = s.recv(4096)

print reply
