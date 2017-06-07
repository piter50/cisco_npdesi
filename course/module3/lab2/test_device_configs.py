#!/usr/bin/env python

import unittest
import requests
import json
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

class TestDeviceConfiguration(unittest.TestCase):

    def test_npdesi_snmp_ro(self):
        """Validate npdesi is a configured RO string
        """

        auth = HTTPBasicAuth('cisco', 'cisco')
        headers = { 'Accept': 'application/vnd.yang.data+json'}
        url = 'http://csr1kv/restconf/api/config/native/snmp-server?deep'
        response = requests.get(url, verify=False, headers=headers, auth=auth)

        parse = json.loads(response.text)
        community_list = parse['ned:snmp-server']['community']
        expected = {'name': 'npdesi', 'RO': [None]}
        is_there = expected in community_list
        self.assertTrue(is_there)


    def test_cisco_snmp_ro(self):
        """Validate cisco is a configured RO string
        """

        auth = HTTPBasicAuth('cisco', 'cisco')
        headers = { 'Accept': 'application/vnd.yang.data+json'}
        url = 'http://csr1kv/restconf/api/config/native/snmp-server?deep'
        response = requests.get(url, verify=False, headers=headers, auth=auth)

        parse = json.loads(response.text)
        community_list = parse['ned:snmp-server']['community']
        expected = {'name': 'cisco', 'RO': [None]}
        is_there = expected in community_list
        self.assertTrue(is_there)

    def test_cisco_secure_snmp_rw(self):
        """Validate cisco_secure is a configured RW string
        """

        auth = HTTPBasicAuth('cisco', 'cisco')
        headers = { 'Accept': 'application/vnd.yang.data+json'}
        url = 'http://csr1kv/restconf/api/config/native/snmp-server?deep'
        response = requests.get(url, verify=False, headers=headers, auth=auth)

        parse = json.loads(response.text)
        community_list = parse['ned:snmp-server']['community']
        expected = {'name': 'cisco_secure', 'RW': [None]}
        is_there = expected in community_list
        self.assertTrue(is_there)


if __name__ == "__main__":
    unittest.main()

              
