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

command_show_version = "show version"

with ConnectHandler(**cisco123) as net_connect:
    output_show_version = net_connect.send_command(command_show_version)

print("Show version:")
print(output_show_version)
print()