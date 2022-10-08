#!/usr/bin/python

from socket import *
import optparse
from threading import *
from termcolor import colored

def connScan(tghost,tport):
	try:
		sock = socket(AF_INET,SOCK_STREAM)
		sock.connect((tghost,tport))
		print(colored("[+] %d/tcp Open" %(tport),'green'))
	except:
		print(colored("[-] %d/tcp Closed" %(tport),'red'))
	finally:
		sock.close()
def portScan(tghost,tport):
	try:
		tgIP =  gethostbyname(tghost)
	except:
		print('Unknown Host %s' %s(tghost))
	try:
		tgname = gethostbyaddr(tgIP)
		print("[+] Scan results for :" +tgname[0])
		
	except:
		print("[+] Scan results for : " +tgIP)
	setdefaulttimeout(1)
	for tp in tport:
		t = Thread(target=connScan,args=(tghost,int(tp)))
		t.start()

def main():
	parser = optparse.OptionParser('Usage of program: '+ '-H <target host> -p <Target Ports> ')
	parser.add_option('-H',dest='tghost',type='string',help='specify target host')
	parser.add_option('-p',dest='tport',type='string',help='specify target ports seperated by comma')
	(options,args) = parser.parse_args()
	tghost = options.tghost
	tport = str(options.tport).split(',')
	if (tghost == None) | (tport[0] == None):
		print(parser.usage)
		exit(0)
	portScan(tghost,tport)


if __name__ == '__main__':
	main()
