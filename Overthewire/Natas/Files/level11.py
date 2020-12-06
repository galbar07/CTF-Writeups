#!/usr/bin/env python

import requests
import base64
import urllib.parse
username = "natas11"
password = "U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"

cookies = {"data" : "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"};
url = 'http://'+username+'.natas.labs.overthewire.org'
session = requests.session()
response = session.get(url, auth = (username, password),cookies = cookies)
content = response.text
#   urldecode = urllib.parse.unquote(session.cookies['data'])
#base64Decode = base64.b64decode(urldecode).hex()

print(content)
