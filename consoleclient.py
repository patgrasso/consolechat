# Console Client
# Patrick Grasso
# Updated October 31, 2013
#
# *NOTE* - Due to the use of the msvcrt module (which gets key
#          input), this client will only work on windows.

import threading, time, sys, socket, os, urllib2
import msvcrt as m

version = "1.0.1"

typing = False
inpstr = ""
name = ""
s = 0
os.system("color bc")
os.system("title Console Chat - v. " + version)

# Network functions
def connectToServer():
    ''' Attempt a connection to the server.'''
    global name, s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '155.246.126.52'
    port = 12345
    print "Attempting to connect to server... (#^.^#)"

    try:
        s.connect((host, port))
        latestVersion = s.recv(1024)
        if version != latestVersion:
            printsrn(" ! There is an updated version of Console Chat available.\n")
            printsrn("   Go to 155.246.126.52/consolechat.exe to get the latest version.\n")
        name = raw_input("Your Name: ")
        s.send("###@@join@@###")
        time.sleep(0.1)
        s.send(name)
        printsrn("Welcome to the chat, " + name + "!")
    except:
        print "Sorry, could not connect   (~_~;)"

def run():
    ''' Continually receives messages from the server.'''
    while 1:
        try:
            case = s.recv(8194)
            if case == "###@@ascii@@###":
                printsrn(s.recv(8194), 0)
            else:
                printsrn(case)
        except:
            print "Lost Connection"
            for x in range(3, 0, -1):
                printsrn(x)
                time.sleep(1)
            break
    quit()

def printsrn(string, linespace=1):
    ''' Prints a string to the screen by flushing the current line
        (by default, this is the user input line), then printing
        the string, then printing the input line 2 lines down.'''
    global typing, inpstr
    if not typing: sys.stdout.write("\n" + string)
    else:
        lineFlush()
        sys.stdout.write(string)
        sys.stdout.write("\n" + "\n"*linespace + name + ": " + inpstr)

def inp():
    ''' Initiates user input. The input is continuous (while 1). Input
        is gathered by collecting each letter at a time until the user
        presses enter, at which point the compiled string is sent to
        the server and a new line is created. This method solves the
        issue of getting raw_input() while trying to print to the
        screen simultaneously.'''
    global typing, inpstr, name
    while 1:
        typing = True
        sys.stdout.write("\n\n" + name + ": ")
        inpstr = ""
        while 1:
            nextChar = ord(m.getch())
            if nextChar == 13:
                if inpstr[:5] == "color":
                    os.system(inpstr)
                    printsrn("  -Color changed to " + inpstr)
                    break
                s.send("###@@chat@@###")
                time.sleep(0.1)
                s.send(inpstr)
                break
            elif nextChar == 255:
                pass
            elif nextChar == 8:
                inpstr = inpstr[:-1]
                lineFlush()
                sys.stdout.write(name + ": " + inpstr)
            else:
                sys.stdout.write(chr(nextChar))
                inpstr += chr(nextChar)

def lineFlush():
    ''' Flush the current line and set the cursor to the beginning.'''
    sys.stdout.write("\r" + " "*79 + "\r")


def header():
    print "                     ______________________________________"
    print "             _______|             CONSOLE CHAT             |_______"
    print "             \      |               v. 1.0.1               |      /"
    print "              \     |            Patrick Grasso            |     /"
    print "              /     |______________________________________|     \ "
    print "             /_________)                                (_________\ "

    
# Begin client
header()
connectToServer()

tS = threading.Thread(target=run)
tI = threading.Thread(target=inp)
tS.start()
tI.start()
