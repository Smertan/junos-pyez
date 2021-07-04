from jnpr.junos import Device
from getpass import getpass
import jnpr.junos.exception

ipadd = input('Enter hostname or IP address: ')
username = input('Enter username: ')
password = getpass('Enter password: ')

try:
    with Device(host=ipadd, user=username, password=password) as dev:
        print('Are we connected?', dev.connected)
        software = dev.rpc.get_software_information()
        host_name = software.findtext("host-name")
        model = software.findtext("product-model")
        version = software.findtext("package-information/comment")
        print('*' * 70,
              "Operational checks".center(70),
              f"\n\nHost-name: {host_name}",
              f"Model: {model}",
              f"Version: {version}",              
              "*" * 70, sep="\n")
except jnpr.junos.exception.ConnectAuthError as autherr:
    print('Check username and password', autherr)
