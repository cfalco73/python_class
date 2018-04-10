

from netmiko import ConnectHandler

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
}

pynet_rtr2 = ConnectHandler(**pynet2)
pynet_rtr2.config_mode()
pynet_rtr2.send_command("logging buffered 20019")
pynet_rtr2.exit_config_mode()
outp = pynet_rtr2.send_command("sh run | in logging")
print(outp)
pynet_rtr2.disconnect()

