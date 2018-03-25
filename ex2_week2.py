#!/usr/bin/env python


import telnetlib
import time


TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main():
    ip_addr = "184.105.247.70"
    username = "pyclass"
    password = "88newclass"

    telnet_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    output = telnet_conn.read_until("sername:", TELNET_TIMEOUT)
    telnet_conn.write(username + '\n')
    output = telnet_conn.read_until("ssword", TELNET_TIMEOUT)
    telnet_conn.write(password + '\n')

    time.sleep(2)

    output = telnet_conn.read_very_eager()
    telnet_conn.write("show ip interface brief" + '\n')
    time.sleep(2)
    output = telnet_conn.read_very_eager()
    print output

    telnet_conn.close()



if __name__ == "__main__":
    main()


