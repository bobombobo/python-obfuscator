import time
import hashlib
import requests
import random
import string
import getopt
import http.cookiejar
import sys
import urllib.parse
import urllib.request
from http.cookies import SimpleCookie
from json import loads as json_loads
from os import environ

def gen_anti_code(code):
  _headers = {"Referer": 'https://rentry.co'}


  class UrllibClient:
      """Simple HTTP Session Client, keeps cookies."""

      def __init__(self):
          self.cookie_jar = http.cookiejar.CookieJar()
          self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookie_jar))
          urllib.request.install_opener(self.opener)

      def get(self, url, headers={}):
          request = urllib.request.Request(url, headers=headers)
          return self._request(request)

      def post(self, url, data=None, headers={}):
          postdata = urllib.parse.urlencode(data).encode()
          request = urllib.request.Request(url, postdata, headers)
          return self._request(request)

      def _request(self, request):
          response = self.opener.open(request)
          response.status_code = response.getcode()
          response.data = response.read().decode('utf-8')
          return response


  def raw(url):
      client = UrllibClient()
      return json_loads(client.get('https://rentry.co/api/raw/{}'.format(url)).data)


  def new(url, edit_code, text):
      client, cookie = UrllibClient(), SimpleCookie()

      cookie.load(vars(client.get('https://rentry.co'))['headers']['Set-Cookie'])
      csrftoken = cookie['csrftoken'].value

      payload = {
          'csrfmiddlewaretoken': csrftoken,
          'url': url,
          'edit_code': edit_code,
          'text': text
      }

      return json_loads(client.post('https://rentry.co/api/new', payload, headers=_headers).data)


  def edit(url, edit_code, text):
      client, cookie = UrllibClient(), SimpleCookie()

      cookie.load(vars(client.get('https://rentry.co'))['headers']['Set-Cookie'])
      csrftoken = cookie['csrftoken'].value

      payload = {
          'csrfmiddlewaretoken': csrftoken,
          'edit_code': edit_code,
          'text': text
      }

      return json_loads(client.post('https://rentry.co/api/edit/{}'.format(url), payload, headers=_headers).data)



  import pickle
  import base64
  def sha256sum(filename):
      h  = hashlib.sha256()
      b  = bytearray(128*1024)
      mv = memoryview(b)
      with open(filename, 'rb', buffering=0) as f:
          for n in iter(lambda : f.readinto(mv), 0):
              h.update(mv[:n])
      return h.hexdigest()
    

  def randstring(length):
    letters = string.ascii_letters
    return ( ''.join(random.choice(letters) for i in range(length)) )


  text = "temp_place_holder"
  eidt_code_raw=randstring(16)
  url=randstring(16)

  response = new(url, eidt_code_raw, text)
  if response['status'] != '200':
      print('error: {}'.format(response['content']))
      try:
          for i in response['errors'].split('.'):
              i and print(i)
          sys.exit(1)
      except:
          sys.exit(1)
  else:
      #print('Url:        {}\nEdit code:  {}'.format(response['url'], response['edit_code']))
      print("success")

  raw_url = "https://rentry.co/"+url+"/raw"


  class RCE:
    def __reduce__(self):
      #with open("payload.py", "r") as file:
      #  payloadfile = file.read()
      #payload = ("python payload.py")
      cmd=(str(final))
      return (eval("exec"), (cmd,))


  #generate payload
  def gp():
    pickled = pickle.dumps(RCE())
    return((base64.urlsafe_b64encode(pickled)).decode('utf-8'))


  code = code
  oaiuwbegiubaw=randstring(12)
  hashcheck='''import requests;import hashlib
def sha256sum(filename):
  h  = hashlib.sha256()
  b  = bytearray(128*1024)
  mv = memoryview(b)
  with open(filename, 'rb', buffering=0) as f:
      for n in iter(lambda : f.readinto(mv), 0):
          h.update(mv[:n])
  return h.hexdigest()

hashval = requests.get("url").text

if (sha256sum(__file__))==(hashval):
  exec("""[ungoiwnbng]""")
else:
  print("invalid code! contact a administrator if you believe this is an error.")'''.replace("url", raw_url)
  final=hashcheck.replace("oaiuwbegiubaw", oaiuwbegiubaw)
  final = final.replace("[ungoiwnbng]", code)
  class RCE:
    def __reduce__(self):
      #with open("payload.py", "r") as file:
      #  payloadfile = file.read()
      #payload = ("python payload.py")
      cmd=(str(final))
      return (eval("exec"), (cmd,))


  #generate payload
  def gp():
    pickled = pickle.dumps(RCE())
    return((base64.urlsafe_b64encode(pickled)).decode('utf-8'))

  batch_code = gp()

  payload = ("import pickle;import base64;pickle.loads(base64.urlsafe_b64decode('payload_eiuahiwuhg'))\n".replace("payload_eiuahiwuhg", str(batch_code)))
  return([payload, url, eidt_code_raw])
  #print(code)
  #print(sha256sum("testcode.py"))

