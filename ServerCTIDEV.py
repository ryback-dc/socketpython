print "--------------------------------------------------------------------------------"
print " PT WAHANA MANDIRI SYDRATAMA"
print " COMPUTER TELEPHONY INTEGRATION SYSTEM"
print " support@whnmandiri.co.id"
print "--------------------------------------------------------------------------------"
print "\n"
print "                             ______  cti-pty"
print "                         ___/_____/\ "
print "                        /         /\\  6.10.1.3.7 "
print "                  _____/__       /  \\ "
print "                _/       /\_____/___ \  Copyright (c) 2016, WHNDevTeam"
print "               //       /  \       /\ \ "
print "       _______//_______/    \     / _\/______ "
print "      /      / \       \    /    / /        /\ "
print "   __/      /   \       \  /    / /        / _\__ "
print "  / /      /     \_______\/    / /        / /   /\ "
print " /_/______/___________________/ /________/ /___/  \ "
print " \ \      \    ___________    \ \        \ \   \  / "
print "  \_\      \  /          /\    \ \        \ \___\/ "
print "     \      \/          /  \    \ \        \  / "
print "      \_____/          /    \    \ \________\/ "
print "           /__________/      \    \  /"
print "           \   _____  \      /_____\/"
print "            \ /    /\  \    /___\/"
print "             /____/  \  \  /"
print "             \    \  /___\/"
print "              \____\/"
print "--------------------------------------------------------------------------------"

import sys
import socket
import threading
from thread import *

print "[INFO] >> load library sys ... "
print "[INFO] >> load library thread... "
print "[INFO] >> load library socket... "


class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

        ##print status Connected and create socket

        print "[SERVER][INFO]>> Successfull create socket on port %s ...." % (self.port)

    def listen(self):
        self.sock.listen(100)
        while True:
            client, address = self.sock.accept()
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

            print "[SERVER][CONNECT] >> client %s %s is connected to server ..." % (address, client)


    def listenToClient(self, client, address):
        size = 1024
        s = socket.socket()
        atghost = '192.168.1.147'
        atgport = 8008

        while True:
            try:
                data = client.recv(size)
                if data:

                    s.send(data)
                    print "[SERVER][CONNECT] >> recieved data on %s %s... " % (address, client)
                    print "[ATG][CONNECT] >> send message %s " % (data)

                    data_reply_atg = s.recv(1024)
                    print "[ATG][CONNECT] >>replay message %s " % (data_reply_atg)

                    response = data_reply_atg
                    client.send(response)
                    print "[SERVER][CONNECT] >> send message %s" % (response)

                else:
                    data_atg = s.recv(size)
                    print "[ATG][CONNECT] >> retrivce message %s" % (data_atg)


            except:
                client.close()
                return False

if __name__ == "__main__":
    #port_num = input("Port? ")
    ThreadedServer('',9000).listen()
