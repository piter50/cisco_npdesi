#!/usr/bin/env python

import requests
import json
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    auth = HTTPBasicAuth('cisco', 'cisco')
    headers = {
        'Content-Type': 'application/json'
    }

    commands = ['vlan 150', 'exit', 'interface Eth2/5', 'switchport', 'switchport access vlan 150']

    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_conf",
            "chunk": "0",
            "sid": "1",
            "input": commands
            "output_format": "json"
        }
    }
    url = 'http://nxosv/ins'

    response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
    rx_object = json.loads(response.text)

    print json.dumps(rx_object, indent=4)

