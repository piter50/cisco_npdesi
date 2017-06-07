#!/usr/bin/env python

from ncclient import manager

if __name__ == '__main__':

    with manager.connect(host='nxosv', port=22, username='cisco', password='cisco',
                         hostkey_verify=False, device_params={'name': 'nexus'},
                         allow_agent=False, look_for_keys=False) as device:

        get_filter = """
                      <show>
                        <hostname>
                        </hostname>
                      </show>
                      """
        nc_get_reply = device.get(('subtree', get_filter))
        print 'Response as XML String: '
        print nc_get_reply.xml

        ns_map = {'mod': 'http://www.cisco.com/nxos:1.0:vdc_mgr'}
        xml_rsp = nc_get_reply.data_ele.find('.//mod:hostname', ns_map)
        value = xml_rsp.text
        print '================================='
        print 'Hostname: ', value

