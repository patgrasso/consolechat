# Console Server
# Patrick Grasso
# Updated October 31, 2013

import socket
import threading
import time

global clients
clients = {}
version = "1.0.1"

def listen():
    ''' Continually listen for connections.'''
    while 1:
        print "Listening..."
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 12345
        s.bind((host, port))
        s.listen(5)
        c, addr = s.accept()
        print "Got connection from " + str(addr)
        tC = threading.Thread(target=clientString, args=(c, addr))
        tC.start()
        clients[c] = []

def clientString(c, addr):
    ''' Client thread. A new client thread starts for each connection.'''
    c.send(version)
    while 1:
        try: msg = c.recv(1024)
        except:
            c.close()
            del clients[c]
            break
        if msg == "###@@join@@###":
            clients[c] += [c.recv(1024)]
            sendAll(" + " + str(clients[c][0]) + " has joined the chat")
        if msg == "###@@chat@@###":
            text = c.recv(8192)
            clients[c] += [text]
            line = str(clients[c][0]) + ": " + text
            print line
            sendAllBut(line, c)
            
def sendAll(message):
    ''' Sends a message to all clients.'''
    for client in clients:
        client.send(message)

def sendTo(message, a):
    ''' Sends a message to a specific client. A socket must be passed in
        as a.'''
    a.send(message)

def sendAllBut(message, a):
    ''' Sends a message to all clients except a (once again, a socket).
        Used primarily to relay messages from one client to all others.'''
    for client in clients:
        if client != a:
            client.send(message)

def timeTag():
    ''' Get the current timestamp.'''
    return "(" + time.strftime("%I:%M:%S %p", time.gmtime()) + "): "

def sendascii(filename):
    ''' Opens a text file "filename" and sends its individual lines as
        messages to all clients.'''
    f = open(filename, 'rb')
    L = f.read().splitlines()
    for x in L:
        sendAll("###@@ascii@@###")
        time.sleep(.25)
        sendAll(x)
        time.sleep(.25)

# Start server
tL = threading.Thread(target=listen)
tL.start()


