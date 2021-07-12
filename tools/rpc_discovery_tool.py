from jnpr.junos import Device
from getpass import getpass
import jnpr.junos.exception
import sys


ipadd = input('Enter hostname or IP address: ')
key_password = getpass('Enter key password: ')

try:
    with Device(host=ipadd, password=key_password) as dev:
        print('Are we connected?', dev.connected)
        try:
            print("*" * 70, "\n")
            if sys.argv[1]:
                for arg in sys.argv[1:]:
                    sys_cmd = dev.display_xml_rpc(arg).tag.replace("-", "_")
                    print(arg, f"= {sys_cmd}", "\n" + "-" * 70)
                print("\n\n" + "*" * 70)
        except IndexError:
            print(
"""
No command entered, i.e.,

python3.py rpc.discovery_tool.py 'show version'
""")
except jnpr.junos.exception.ConnectAuthError as autherr:
    print('Check key password', autherr)
