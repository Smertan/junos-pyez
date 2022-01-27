from jnpr.junos import Device
from getpass import getpass
import jnpr.junos.exception
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.elsethernetswitchingtable import ElsEthernetSwitchingTable


ipadd = input('Enter hostname or IP address: ')
key_password = getpass('Enter key password: ')


def get_arp_info(ip_addr, dev):
    """Get the mac address from the arp table for the given ip
    address.
    """
    arp_table = ArpTable(dev)
    arp_table.get(hostname=ip_addr)
    print(arp_table.items())
    items = len(arp_table.keys())
    for ip in range(items):
        if arp_table[ip]['ip_address'] == ip_addr:
            print("\n\nFound the ip address:", arp_table[ip]['ip_address'])
            return arp_table[ip]['mac_address']
    return


def get_els_ether_table(mac_addr, dev):
    """Get the physical interface name from the ethernet table of the given
    IP address.
    """
    ether = ElsEthernetSwitchingTable(dev)
    ether.get(mac_addr)
    print("\n\nFound the interface: ", ether[mac_addr]['logical_interface'],
          "\n\n", end="-" * 70)
    print()


try:
    with Device(host=ipadd, password=key_password) as dev:
        print('Are we connected?', dev.connected)
        ip_addr = input("Enter the IP address to locate: ")
        mac_addr = get_arp_info(ip_addr, dev)
        if mac_addr:
            get_els_ether_table(mac_addr, dev)
        else:
            print("Not Found")
except jnpr.junos.exception.ConnectAuthError as autherr:
    print('Check key password', autherr)
