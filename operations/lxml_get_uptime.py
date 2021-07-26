from jnpr.junos import Device
from getpass import getpass
import jnpr.junos.exception


ipadd = input('Enter hostname or IP address: ')
key_password = getpass('Enter key password: ')

try:
    with Device(host=ipadd, password=key_password) as dev:
        print('Are we connected?', dev.connected)
        sys_uptime = dev.rpc.get_system_uptime_information(normalize=True)
        uptime = sys_uptime.findtext("uptime-information/up-time")
        seconds = sys_uptime.find("uptime-information/up-time").attrib['seconds']
        print("\n" + repr(uptime))
        print(f"Total in seconds = {seconds}")
        print()
except jnpr.junos.exception.ConnectAuthError as autherr:
    print('Check key password', autherr)
