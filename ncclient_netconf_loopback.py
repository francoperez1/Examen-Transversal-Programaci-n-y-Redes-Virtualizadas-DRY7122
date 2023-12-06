import xml.dom.minidom
from ncclient import manager

m = manager.connect(
    host="192.168.56.106",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

#configuracion de loopback del router CSR1000v
netconf_loopback = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>1</name>
                <description>Loopback1 ET</description>
                <ip>
                    <address>
                        <primary>
                            <address>1.1.1.1</address>
                            <mask>255.255.255.255</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()
)