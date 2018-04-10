

from netmiko import ConnectHandler

pynet1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': '88newclass',
}

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
}

juniper = {
    'device_type': 'juniper',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': '88newclass',
}


for router in (pynet1, pynet2, juniper):
    n_connect = ConnectHandler(**router)
    outp = n_connect.send_command("show arp")
    print("Router: {}".format(n_connect.ip))
    print(outp)


