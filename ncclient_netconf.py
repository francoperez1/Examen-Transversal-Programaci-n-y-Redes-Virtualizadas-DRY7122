import xml.dom.minidom
from ncclient import manager

m = manager.connect(
    host="192.168.56.106",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

#configuracion de hostname del router CSR1000v
netconf_hostname = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>Perez-Guajardo</hostname>
    </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_hostname)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()
)