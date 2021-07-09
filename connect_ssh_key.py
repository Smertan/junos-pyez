from jnpr.junos import Device
from getpass import getpass
import jnpr.junos.exception

ipadd = input('Enter hostname or IP address: ')
key_password = getpass('Enter password: ')

try:
    with Device(host=ipadd, password=key_password) as dev:
        print('Are we connected?', dev.connected)
except jnpr.junos.exception.ConnectAuthError as autherr:
    print('Check key password', autherr)
