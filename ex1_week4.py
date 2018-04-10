
import paramiko
import time

ip_addy = "184.105.247.71"
username = "pyclass"
password = "88newclass"

remote_conn_p=paramiko.SSHClient()
remote_conn_p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_p.connect(ip_addy, username=username, password=password, look_for_keys=False, 

allow_agent=False)

remote_conn = remote_conn_p.invoke_shell()
remote_conn.send("terminal length 0\n")
time.sleep(1)
remote_conn.send("show version\n")
time.sleep(3)
out = remote_conn.recv(10000)
print out


