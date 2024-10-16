#!/usr/bin/python

from socket import *
import optparse
from threading import *
from termcolor import colored

def connScan(host, port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(2)
    try:
        sock.connect((host, port))
        banner = sock.recv(1024).decode("utf-8")
        banner = str(banner).strip("\n")
        print(colored(f"[+] {port}/tcp is opened: {banner}", 'green'))
    except:
        return
    finally:
        sock.close()

def portScan(trgtHost, trgtPorts):
    setdefaulttimeout(2)
    try:
        tgtIP = gethostbyname(trgtHost)
    except:
        print(f"unknown Host {trgtHost}")
    try:
        tgtName = gethostbyaddr(tgtIP)
        print("[+] Scan result for: " + tgtName[0])
    except:
        print("[+] Scan result for: " + tgtIP)
    for tgtPort in range(1,6000):
        t = Thread(target=connScan, args=(trgtHost, int(tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser('Usage of the program: ' + '-H <taget host> -p <target port>')
    parser.add_option('-H', dest='trgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='trgtPort', type='string', help='specify target ports sperated by comma')
    options, args = parser.parse_args()
    trgtHost = options.trgtHost
    trgtPorts = str(options.trgtPort).split(',')
    if (trgtHost == 'None') or (trgtPorts[0] == 'None'):
        print(parser.usage)
        exit(0)
    portScan(trgtHost, trgtPorts)

if __name__ == "__main__":
    main()