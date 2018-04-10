

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


for router in (pynet1, pynet2):
    n_connect = ConnectHandler(**router)
    n_connect.send_config_from_file(config_file="config_file.txt")
    outp = n_connect.send_command("sh run | in logging")
    print("Router: {}".format(n_connect.ip))
    print(outp)
    
