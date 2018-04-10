
import pexpect
import time

ip_addy = "184.105.247.71"
username = "pyclass"
port = 22
password = "88newclass"

ssh_c = pexpect.spawn("ssh -l {} {} -p {}".format(username, ip_addy, port))
ssh_c.timeout = 3
ssh_c.expect("ssword")
ssh_c.sendline(password)
ssh_c.expect("pynet-rtr2")

ssh_c.sendline("terminal length 0")
ssh_c.expect("pynet-rtr2")

ssh_c.sendline("show ip int brief")
ssh_c.expect("pynet-rtr2")

print ssh_c.before


