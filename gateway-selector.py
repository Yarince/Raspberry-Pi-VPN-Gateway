#!/usr/bin/env python

import os
import sys

import json
import subprocess
import time
import requests


# URL to the NordVPN server connection tool obtained from the browser
url = "https://nordvpn.com/wp-admin/admin-ajax.php?action=servers_recommendations&filters={%22country_id%22:" + sys.argv[1] + "}" # Insert URL here

def find_openvpn_connection():
    response = requests.get(url)

    if len(response.text) != 2:
        nvpn_response = json.loads(response.text)
        vpn_info = nvpn_response[0]
        vpn_info_hostname = vpn_info["hostname"]
        vpn_file = vpn_info_hostname + ".udp.ovpn"
        print(vpn_file)

if __name__ == "__main__":
    find_openvpn_connection()
