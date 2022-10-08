#!/usr/bin/python

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("[*]Enter The Host To Scan : ")
#port = int(input("[*]Enter The Port To Scan : "))

def portscanner(port):
	if sock.connect_ex((host,port)):
		print(colored("[!!]Port %d is closed" %(port),'red'))
	else:
		print(colored("[+]Port %d is open" %(port),'green'))


# scan first 1000 ports

for i in range(1,1001):
	portscanner(i)

