## pearl pearl pearl

pearlpearlpearlpearlpearlpearlpearlpearlpearlpearlpearlpearlpearlpearlpearl

**ractf{p34r1_1ns1d3_4_cl4m}**

**Solution:** When we connect to server we are given a weird stream of data that contain ctf{pearlpearlpearl}.

After longue research on it, a message was hidden by using a carriage return symbol so when you are connected to the server and the output is printed to the terminal you can't see the message as the symbol makes the terminal overwrite the data in the line, but if you check the actual data printed by the server you can see the message.
So, I wrote a short script which connects to the server, reads the data and prints it to the screen without special symbols taking effect (and most importantly carriage return), but it didnt work, it's seems that even though there are a lot of carriage return symbols in the data there aren't any hidden messages.

With that in mind, I wrote a short script which creates a empty string, reads until an end of a false flag and check if the symbol afterwards is new line or carriage return and append 0 or 1 to the string accordinaly, in the end it encodes the binary string to ascii characters and prints them:

```python 3
from pwn import remote
import binascii
host = "88.198.219.20"
port = 22324
s = remote(host, port)
flag = ''
try:
    while 1:
        s.recvuntil("}")
        end = str(s.recv(1))
        if 'r' in end:
            flag += '0'
        else:
            flag += '1'
except EOFError:
    print(''.join([chr(int(flag[i:i + 8], 2)) for i in range(0, len(flag), 8)]))
```
and I got the flag:

ractf{p34r1_1ns1d3_4_cl4m}

**Resources:**
* Writeup for clam clam clam challenge from AngstromCTF 2020: https://ctftime.org/writeup/18869
