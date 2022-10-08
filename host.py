#!/usr/bin/python

import socket

hostname = "www.google.com"

ipAddress = socket.gethostbyname(hostname)

print("IP Address of the host name  {} is {}".format(hostname,ipAddress))
