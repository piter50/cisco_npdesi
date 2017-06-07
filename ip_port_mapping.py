#!/usr/bin/env python

from cisco import clid
import json

if __name__ == '__main__':

    arp_table = clid('show ip arp vrf all')

    arp_tabled = json.loads(arp_table)
    arp_entries = arp_tabled['TABLE_vrf']['ROW_vrf']['TABLE_adj']['ROW_adj']
    if isinstance(arp_entries, dict):
        arp_entries_list = [arp_entries]
    combined_table = {}
    for entry in arp_entries:
        combined_table[entry.get('mac')] = {}
        combined_table[entry.get('mac')]['ipaddr'] = entry['ip-addr-out']

    mac_table = clid('show mac address-table')
    mac_tabled = json.loads(mac_table)
    mac_entries_list = mac_tabled['TABLE_mac_address']['ROW_mac_address']

    if isinstance(mac_entries_list, dict):
        mac_entries_list = [mac_entries_list]
    for entry in mac_entries_list:
        if not combined_table.get(entry.get('disp_mac_addr')):
            combined_table[entry.get('disp_mac_addr')] = {}
        combined_table[entry.get('disp_mac_addr')]['interface'] = entry.get('disp_port')
        combined_table[entry.get('disp_mac_addr')]['vlan'] = entry.get('disp_vlan')
    # print combined_table
    print '{: <14}{: <15}{: <8}{: <15}'.format('IP ADDR', 'INTERFACE', 'VLAN', 'MAC ADDR')
    for item, value in combined_table.items():
        print '{: <14}{: <15}{: <8}{: <15}'.format(value.get('ipaddr'), value.get('interface'),
                                                   value.get('vlan'), item)
