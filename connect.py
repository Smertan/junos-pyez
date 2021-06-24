from jnpr.junos import Device
from getpass import getpass
import jnpr.junos.exception

ipadd = input('Enter hostname or IP address: ')
username = input('Enter usename: ')
password = getpass('Enter password: ')

try:
    with Device(host=ipadd, user=username, password=password) as dev:
        print('Are we connected?', dev.connected)
except jnpr.junos.exception.ConnectAuthError as autherr:
    print('Check username and password', autherr)
