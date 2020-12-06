#!/usr/bin/python3

import requests

username = "natas24"
password = "OsRmXFguozKpTZZ5X14zNO43379LZveg"

url = 'http://'+username+'.natas.labs.overthewire.org/'
session = requests.session()
data = {'passwd' : '0'}
response = session.post(url, data = data, auth = (username, password))
content = response.text
print(content)
