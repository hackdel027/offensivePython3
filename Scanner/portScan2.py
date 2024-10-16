#!/usr/bin/python

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#                    ipv4 address      tcp connexion
sock.settimeout(2)

host = input("[+] Enter The Host To Scan: ")

def portscanner(port):
    if sock.connect_ex((host, port)):
        print(colored(f"[!!] Port {port} is closed", 'red'))
    else: print(colored(f"[+] Port {port} is opened",'green'))

for port in range(445, 500):
    portscanner(port)
    