#!/usr/bin/env python

from ncclient import manager

if __name__ == '__main__':

    with manager.connect(host='nxosv', port=22, username='cisco', password='cisco',
                         hostkey_verify=False, device_params={'name': 'nexus'},
                         allow_agent=False, look_for_keys=False) as device:

        get_filter = """
                      <show>
                        <interface>
                        </interface>
                      </show>
                      """
	commands = ['conf t', 'int Ethernet2/6', 'switchport', 'desc Configured by ncclient']
        nc_config_reply = device.exec_command(commands)
        print nc_config_reply.xml
        nc_get_reply = device.get(('subtree', get_filter))
        print 'Response as XML String: '
        print nc_get_reply.xml
