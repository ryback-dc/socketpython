print "--------------------------------------------------------------------------------"
print " PT WAHANA MANDIRI SYDRATAMA"
print " COMPUTER TELEPHONY INTEGRATION SYSTEM"
print " support@whnmandiri.co.id"
print "--------------------------------------------------------------------------------"
print "\n"
print "                             ______  cti-pty"
print "                         ___/_____/\ "
print "                        /         /\\  6.10.1.5.7 "
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
from multiprocessing import Process


print "[INFO] >> load library sys ... "
print "[INFO] >> load library thread... "
print "[INFO] >> load library socket... "
print "[INFO] >> loasd library multiprocessing ..."

class ThreadedServer(object):
    def __init__(self, host, port):

        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        print "[SERVER][INFO]>> Successfull create socket on port %s ...." % (self.port)

    def listen(self):
        self.sock.listen(100)

        atg     = socket.socket()
        atghost = '192.168.1.147'
        atgport = 8008
        atg.connect((atghost, atgport))
        print "[ATG][CONNECT] >> Connected client to atg server  %s %s ..." % (atghost, atgport)

        while True:
            client, address = self.sock.accept()
            d = threading.Thread(target = self.listenToClient,args = (client,address,atg)).start()
            e = threading.Thread(target = self.listenToATG,args = (client,address,atg)).start()

            #d.startdaemon(True)
            #d.join()
            #e.join()

            print "[SERVER][CONNECT] >> client %s %s is connected to server ..." % (address, client)


    def listenToClient(self, client, address, atg):
        size    = 1024
        while True:
            try:
                    data = client.recv(size)
                    if data:

                        atg.send(data)
                        print "[SERVER][CONNECT] >> recieved data on %s %s... " % (address, client)
                        print "[ATG][CONNECT] >> send message %s " % (data)

                    else :
                        print "no data"

            except:
               client.close()
               return False

    def listenToATG(self, client, address, atg) :
        size  = 5000
        while True :
            try :
                data = atg.recv(size)
                if data :

                    print "[ATG][CONNECT] >>replay message %s " % (data)

                    response = data
                    client.send(response)
                    print "[SERVER][CONNECT] >> send message %s" % (response)

                else :

                    print "error"

            except :
                atg.close()
                return False


if __name__ == "__main__":
    #port_num = input("Port? ")
    ThreadedServer('',9000).listen()
