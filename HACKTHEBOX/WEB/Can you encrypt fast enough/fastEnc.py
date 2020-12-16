import requests, hashlib
from bs4 import BeautifulSoup
url = 'http://167.99.81.99:30673/'
s = requests.session()
reqs = s.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
str = soup.h3.string
hash = hashlib.md5(str.encode()).hexdigest()
myobj = {'hash': hash}
flag = s.post(url, data=myobj)
print(flag.text)
