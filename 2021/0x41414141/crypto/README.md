# eazy RSA (445)
> c = 3708354049649318175189820619077599798890688075815858391284996256924308912935262733471980964003143534200740113874286537588889431819703343015872364443921848 <br>
> e = 16 <br>
> p = 75000325607193724293694446403116223058337764961074929316352803137087536131383 <br>
> q = 69376057129404174647351914434400429820318738947745593069596264646867332546443 <br>

## Solution
```sage
ZeroDivisionError: inverse of Mod(16, 5203226874048586660123187369475542584442690830335849146139399959453354953924976900388993415470710574187687844214029203747760116730703556445063231528642844) does not exist
```
[Rabin cryptosystem](https://en.wikipedia.org/wiki/Rabin_cryptosystem) and as Wiki says

*The message **m** can be recovered from the ciphertext **c** by taking its square root modulo n as follows.*

In this case we can recover **m** by repeatedly taking ciphertext's (c) square root modulo n as follows,

```py
from Crypto.Util.number import *

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def decrypt(c):
    mp = pow(c, (p+1)//4, p)
    mq = pow(c, (q+1)//4, q)
    r1 = (yp*p*mq + yq*q*mp) % n
    r2 = n-r1 
    r3 = (yp*p*mq - yq*q*mp) % n
    r4 = n-r3
    return (r1,r2,r3,r4)


c = [3708354049649318175189820619077599798890688075815858391284996256924308912935262733471980964003143534200740113874286537588889431819703343015872364443921848]
p = 75000325607193724293694446403116223058337764961074929316352803137087536131383
q = 69376057129404174647351914434400429820318738947745593069596264646867332546443
n = p*q

# Rabin's test
assert p % 4 == 3
assert q % 4 == 3

_, yp, yq = egcd(p,q)
# print(yp,yq)

for i in range(4):
    pts = []
    for ct in c:
        pts += decrypt(ct)
    c = pts
for m in c:
    dec = long_to_bytes(m)
    if b'flag' in dec:
        print(dec)

# flag{d0nt_h4v3_4n_3v3n_3_175_34sy!!!}
```
