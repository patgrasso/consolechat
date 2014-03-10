                        ______________________________________
                _______|                                      |_______
                \      |             CONSOLE CHAT             |      /
                 \     |            Patrick Grasso            |     /
                 /     |______________________________________|     \
                /_________)                                (_________\ 

Welcome to Console Chat!

~~ Description ~~

Console chat is a client-server chat program that utilizes TCP/IP connection
protocol to communicate plaintext messages between clients. The client program
runs from within the windows command prompt (hence console) and accesses some
of the features of the command prompt in order to create an aesthetically
pleasing user interface.


~~ Requirements ~~

The client program (if executed from the .py file) should be run through the
command prompt. It will run successfully from a python interpreter, although
some of the features will not be accessible (such as color scheme control).

Additionally, the client requires a file to be in the same directory,
named host_ip.txt, in order to connect to a server (this allows for the user
to connect to different servers and allows me to omit hard-coding my IP
address into the program).


~~ Features ~~

The server is able to send an ascii-art image to the clients through the command:

	sendascii(filename)

The filename is a text file with the ascii-art image stored in it. In order to
not confuse the packet queue, the lines are sent one by one, with a delay in
between each.

Clients can change the color of their console by using the DOS command:

	color [attr]

The parameter [attr] is comprised of two hexidecimal digits which correspond
to 16 color options. The first digit indicates the background color, the second
the foreground (text) color. For more info, visit the command prompt and type
	
	color ?

for the documentation and color options.


~~ Enjoy! ~~

For questions, contact me through github!
