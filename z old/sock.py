#Sockets and json
#import socket
#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('data.pr4e.org', 80))
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#mysock.send(cmd)
#
#while True:
#    data = mysock.recv(512)
#    if(len(data)< 1):
#        break
#    print(data.decode())
#mysock.close()

#import urllib.request, urllib.parse, urllib.error
#fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#for line in fhand :
#    line = line.decode().split()
#    print(line)
#print(len(line))

#import urlibb.request, urllib.parse, urllib.error
#from bs4 import BeautifulSoup

#url = input('Enter - ')
#html = urllib.request.urlopen(url).read()
#soup = BeautifulSoup(html, 'html.parser')
#
#tags = soup('a')
#for tag in tags:
#    print(tag.get(href, None))

import json
data = '''{
"name" : "chuck",
"phone" : {
"type" : "inl",
"number" : "423"
},
"email" : {
   "hide" : "yes"
    }
}'''

info = json.loads(data)
print(info)
print('Name', info["name"])
print('Hide:',info["email"]["hide"])
