#!/usr/bin/python

import socket
from termcolor import colored
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)

host = input("[+] Enter The host to scan: ")
port = int(input("[+] Enter The port to scan: "))

def portscanner(port):
    if sock.connect_ex((host, port)):
        print(colored(f"[!!] The port {port} is closed !"))
    else: print(colored(f"[+] The port {port} is opened."))

portscanner(port)