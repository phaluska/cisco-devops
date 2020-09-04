#!/usr/bin/env python

import sys
import json
import requests

if len(sys.argv) == 2:
    url = "http://{}/api/v1/inventory/devices".format(sys.argv[1])
else:
    url = input("Enter the server and port info : ") 
    url = "http://{}/api/v1/inventory/devices".format(url)


DATA = [
    {
        "device_type": "switch",
        "hostname": "nyc-rt01",
        "ip_address": "10.100.10.11",
        "role": "dc-spine",
        "site": "nyc",
        "os": "ios",
        "username": "admin",
        "password": "Cisco123"
    },
    {
        "device_type": "switch",
        "hostname": "nyc-rt02",
        "ip_address": "10.100.10.12",
        "role": "dc-spine",
        "site": "nyc",
        "os": "ios",
        "username": "admin",
        "password": "Cisco123"
    },
    {
        "device_type": "switch",
        "hostname": "rtp-rt01",
        "ip_address": "10.100.20.11",
        "role": "dc-spine",
        "site": "rtp",
        "os": "ios",
        "username": "admin",
        "password": "Cisco123"
    },
    {
        "device_type": "switch",
        "hostname": "rtp-rt02",
        "ip_address": "10.100.20.12",
        "role": "dc-spine",
        "site": "rtp",
        "os": "ios",
        "username": "admin",
        "password": "Cisco123"
    }
]

headers = {'content-type': 'application/json'}
for payload in DATA:
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    if r.status_code == 201:
        print("{}: Added successfully".format(payload["hostname"]))
    else:
        print(r.text, r.content, r.json, r.url)
        print("{}: FAILED to add".format(payload["hostname"]))

