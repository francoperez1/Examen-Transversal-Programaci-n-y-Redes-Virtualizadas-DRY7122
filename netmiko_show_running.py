import requests
import netmiko
import json
from netmiko import ConnectHandler

cisco123 = {
    "ip": "192.168.56.106",
    "device_type": "cisco_ios",
    "username": "cisco",
    "password": "cisco123!"
}

command = "show running"

with ConnectHandler(**cisco123) as net_connect:
    output = net_connect.send_command(command)

print()
print(output)
print()