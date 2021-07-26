from jnpr.junos import Device
from getpass import getpass
import jnpr.junos.exception


ipadd = input('Enter hostname or IP address: ')
key_password = getpass('Enter key password: ')

try:
    with Device(host=ipadd, password=key_password) as dev:
        print('Are we connected?', dev.connected)
        interfaces = dev.rpc.get_interface_information(normalize=True)
        interface_list = interfaces.findall(
                "physical-interface/[oper-status='up']/name")
        print("Interface List".center(70, "*"), "\n")
        for interface in interface_list:
            if "ge-" in interface.text:
                print(interface.text)
except jnpr.junos.exception.ConnectAuthError as autherr:
    print('Check key password', autherr)
