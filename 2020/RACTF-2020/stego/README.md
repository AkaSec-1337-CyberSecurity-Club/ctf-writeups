## Mad CTF Disease
Todo:\
[x] Be a cow\
[x] Eat grass\
[x] Eat grass\
[x] Eat grass\
[ ] Find the flag

**ractf{exp3rt-mo0neuv3r5}**

**Solution:**

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/635278809741918218/1033552660957237338/unknown.png">
</p>

First thing I do when faced with images is to check strings, and also i use binwalk to check if there are any embedded files in the images, as expected binwalk finds nothing in this image, afterwards I check using steghide also for embedded files, It supposed to do a better job but I mostly use it by habit because binwalk almost always finds the same files.

After using steghide we manage to extract a file if we take a look at the file steghide found we see a really bizzare text constructed only by moo's:

```
OOOMoOMoOMoOMoOMoOMoOMoOMoOMMMmoOMMMMMMmoOMMMMOOMOomOoMoOmoOmoomOo
MMMmoOMMMMMMmoOMMMMOOMOomOoMoOmoOmoomOoMMMmoOMMMMMMmoOMMMMOOMOomOo
MoOmoOmooOOOmoOOOOmOomOoMMMmoOMMMMOOMOomoOMoOmOomoomOomOoMMMmoOmoO
MMMMOOMOomoOMoOmOomoomOomOomOoMMMmoOmoOmoOMMMMOOMOomoOMoOmOomoomoO
MoOMoOMoomOoOOOmoOOOOmOomOoMMMmoOMMMMOOMOomoOMoOmOomoomOomOoMMMmoO
moOMMMMOOMOomoOMoOmOomoomoOMoOMoomOoOOOmoOOOOmOomOoMMMmoOMMMMOOMOo
moOMoOmOomoomOomOoMMMmoOmoOMMMMOOMOomoOMoOmOomoomoOMoOMoOMoOMoomOo
OOOmoOOOOmOomOoMMMmoOMMMMOOMOomoOMoOmOomoomOomOoMMMmoOmoOMMMMOOMOo
moOMoOmOomoomOomOomOoMMMmoOmoOmoOMMMMOOMOomoOMoOmOomoomoOMoOMoOMoO
MoOMoomOoOOOmoOOOOmOomOoMMMmoOMMMMOOMOomoOMoOmOomoomOomOoMMMmoOmoO
MMMMOOMOomoOMoOmOomoomoOMoOMoOMoOMoOMoOMoOMoomOoOOOmoOOOOmOomOoMMM
moOMMMMOOMOomoOMoOmOomoomOomOoMMMmoOmoOMMMMOOMOomoOMoOmOomoomOomOo
mOoMMMmoOmoOmoOMMMMOOMOomoOMoOmOomoomoOMoOMoOMoOMoOMoOMoOMoOMoOMoO
MoOMoOMoomOoOOOmoOOOOmOomOoMMMmoOMMMMOOMOomoOMoOmOomoomOomOoMMMmoO
moOMMMMOOMOomoOMoOmOomoomoOMoOMoOMoOMoOMoOMoomOoOOOmoOOOOmOomOoMMM
moOMMMMOOMOomoOMoOmOomoomOomOoMMMmoOmoOMMMMOOMOomoOMoOmOomoomOomOo
mOoMMMmoOmoOmoOMMMMOOMOomoOMoOmOomoomoOMoOMoOMoOMoOMoOMoOMoOMoOMoo
mOoOOOmoOOOOmOomOoMMMmoOMMMMOOMOomoOMoOmOomoomOomOoMMMmoOmoOMMMMOO
MOomoOMoOmOomoomoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoO
MoomOoOOOmoOOOOmOomOomOoMMMmoOmoOMMMMOOMOomoOMoOmOomoomOomOomOoMMM
moOmoOmoOMMMMOOMOomoOMoOmOomoomoOMoOMoOMoOMoomOoOOOmoOOOOmOomOoMMM
moOMMMMOOMOomoOMoOmOomoomOomOoMMMmoOmoOMMMMOOMOomoOMoOmOomoomOomOo
mOoMMMmoOmoOmoOMMMMOOMOomoOMoOmOomoomoOMoOMoOMoomOoOOOmoOOOOmOomOo
MMMmoOMMMMOOMOomoOMoOmOomoomOomOoMMMmoOmoOMMMMOOMOomoOMoOmOomoomOo
mOomOoMMMmoOmoOmoOMMMMOOMOomoOMoOmOomoomoOMoOMoOMoOMoOMoomOoOOOmoO
OOOmOomOomOoMMMmoOmoOMMMMOOMOomoOMoOmOomoomoOMoOMoOMoOMoOMoOMoOMoO
MoOMoOMoOMoOMoOMoOMoomOoOOOmoOOOOmOomOoMMMmoOMMMMOOMOomoOMoOmOomoo
mOomOoMMMmoOmoOMMMMOOMOomoOMoOmOomoomoOMoOMoOMoOMoOMoOMoOMoOMoOMoO
MoOMoOMoOMoOMoomOoOOOmoOOOOmOomOoMMMmoOMMMMOOMOomoOMoOmOomoomOomOo
MMMmoOmoOMMMMOOMOomoOMoOmOomoomoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoO
MoOMoOMoOMoOMoomOoOOOmoOOOOmOomOomOoMMMmoOmoOMMMMOOMOomoOMoOmOomoo
moOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoomOoOOOmoOOOO
mOomOoMMMmoOMMMMOOMOomoOMoOmOomoomOomOoMMMmoOmoOMMMMOOMOomoOMoOmOo
moomoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoomOoOOOmoOOOOmOo
mOoMMMmoOMMMMOOMOomoOMoOmOomoomOomOoMMMmoOmoOMMMMOOMOomoOMoOmOomoo
moOMoOMoOMoOMoOMoOMoomOoOOOmoOOOOmOomOoMMMmoOMMMMOOMOomoOMoOmOomoo
mOomOoMMMmoOmoOMMMMOOMOomoOMoOmOomoomOomOomOoMMMmoOmoOmoOMMMMOOMOo
moOMoOmOomoomoOMoOMoOMoOMoOMoOMoomOoOOOmoOOOOmOomOoMMMmoOMMMMOOMOo
moOMoOmOomoomOomOoMMMmoOmoOMMMMOOMOomoOMoOmOomoomOomOomOoMMMmoOmoO
moOMMMMOOMOomoOMoOmOomoomoOMoOMoOMoOMoOMoOMoOMoomOoOOOmoOOOOmOomOo
mOoMMMmoOmoOMMMMOOMOomoOMoOmOomoomOomOomOoMMMmoOmoOmoOMMMMOOMOomoO
MoOmOomoomoOMoOMoOMoOMoomOoOOOmoOOOOmOomOoMMMmoOMMMMOOMOomoOMoOmOo
moomOomOoMMMmoOmoOMMMMOOMOomoOMoOmOomoomOomOomOoMMMmoOmoOmoOMMMMOO
MOomoOMoOmOomoomoOMoOMoOMoomOoOOOmoOOOOmOomOomOoMMMmoOmoOMMMMOOMOo
moOMoOmOomoomOomOomOoMMMmoOmoOmoOMMMMOOMOomoOMoOmOomoomoOMoOMoOMoO
MoOMoOMoomOoOOOmoOOOOmOomOoMMMmoOMMMMOOMOomoOMoOmOomoomOomOoMMMmoO
moOMMMMOOMOomoOMoOmOomoomOomOomOoMMMmoOmoOmoOMMMMOOMOomoOMoOmOomoo
moOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoOMoomOo
```

I recognized this text when I first saw this as the programming language called COW, an esoteric programming language created in the 90's, Now we only need to find an interpreter for this code, I used a random one after a quick google search and run it on the code:

![](https://cdn.discordapp.com/attachments/635278809741918218/1033553913049272441/unknown.png)

and we got our cow-scented flag.

**Resources:**
* steghide: http://steghide.sourceforge.net/
* COW programming language: https://esolangs.org/wiki/COW
* COW interpreter: http://www.frank-buss.de/cow.html

