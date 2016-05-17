import socket	
import urlparse

#set host name and port number
host = ""
port = 4000

#creat AF_NET, STREAM socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("socket created")
k_v = {}
#bind socket to host and port
s.bind((host,port))

while True:
    s.listen(5)

#create connection with client
client, address = s.accept() 
print ("Connection from", address)

#parse url and get and set keyvalues
def parse_for_keyvalue():
    url = "http://localhost:4000/set?somekey=somevalue"
    rl =  urlparse.urlsplit(url)
    print url

parse_for_keyvalue()
 
