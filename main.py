#no matter what an obfuscator is not 100% fool proof
#whilst there are many layers, and complex ideas
#a person determined enough could always crack your program
#python is a very easy program to crack, concider using
#more complex languages or porting to said langauge
#like c, .net, ect...
from tryImports import *
try_all_imports()
import time
import subprocess
import hashlib

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

from modules.errorencryptcode import *
from modules.base64_layer1 import *
from modules.binary_layer2 import *
from modules.split_layer4 import *
from modules.secondarybase64_layer5 import *
from modules.pickle_layer6 import *
from modules.url_obfuscation1 import *
from modules.anti_tamper import *

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

#options :)

layers = [6, 2, 4, 3, 5, 1]

custom_input = False
custom_output = False
speed_test = False
add_vm_detection_to_script = False
use_pickle_serialization = False #May fix "killed" error
minfiy_original_code = True
add_error_encryption = False
do_ast_encrypt = False
url_obfuscate = False
var_type = 3
code_url = "https://raw.githubusercontent.com/bobombobo/Roblox-group-scrapper/main/scrapper.py"
#code_url = "https://hastebin.com/raw/atoruxezef"

#end of options

#code unless custom input :) used for testing mainly
code=('''print("balls!")''')

if url_obfuscate==True:
  og_code = requests.get(code_url).text
  code = url_obfuscation1(code_url)
  code= "import requests\n"+code

if minfiy_original_code==True:
  import python_minifier
  code = (python_minifier.minify(code))


if custom_input == True:
  print("Select the file to encrypt: ")
  print("Example: code.py, code.txt, ect...")
  file_input = input()
  fopening = open(file_input, "r")
  code = (fopening.read())
else:
  file_input = code

if add_vm_detection_to_script == True:
  asdf = open("vmcheck_code.txt", "r")
  vmcheck_code = (asdf.read())
  code = (vmcheck_code+"\n"+code)

if custom_output == True:
  file_output = input("Output file: ")
else:
  file_output = ("obfuscated.py")

og_code = code


print("Thank you for using my python obfuscator!")
print("Created by boboMbobo | https://github.com/bobombobo")

print("Code input: " + og_code)
#print("Output file: " + file_output)
print("--------------------------------------")
if 1 in layers:
 print("base64 (1) ✅")
if 2 in layers: 
  print("binary & list ✅")
if 3 in layers:
  print("splitting ✅")
if 4 in layers:
  print("base64 (2) ✅")
if 5 in layers:
  print("pickle ✅")
print("--------------------------------------")
if url_obfuscate==True:
  print("using url obfuscation for code (make sure url points to raw python code)")
  print("--------------------------------------")

start = time.time()

if var_type == 1:
    whathtenuts = [str(1),str(0)]
elif var_type == 2:
    whathtenuts = ["I", "l"]
elif var_type == 3:
    whathtenuts = ["O", "0"]
else:
    print("Dude.... not a list type available")
dudewhatthenuts = "nil"
if var_type == 1 or var_type == 3:
    dudewhatthenuts = "O"
else:
    dudewhatthenuts = ""

if add_error_encryption == True:
  code = errorencryptcode(code)


for x in layers:

  if x==1:
    code = base64_layer1(code, whathtenuts, dudewhatthenuts)

  #Check in the module file to see what the numbers doe and such. I explain it there 
  #variable_ammount_lenght, toup_text_ammount, ammount, top_layers
  if x==2:
    code = binary_layer2(code, whathtenuts, dudewhatthenuts,10, 10, 1, 5)

  #code = list_layer3(code, whathtenuts, dudewhatthenuts, top_text_code)
  if x==3:
    code = split_layer4(code, whathtenuts, dudewhatthenuts)

  if x==4:
    code = secondarybase64_layer5(code)

  if x==5:
    code = pickle_layer6(code)

  if x==6:
    the_stuff = gen_anti_code(code)
    code=the_stuff[0]


if do_ast_encrypt == True:
  print("Starting secondary ast obfuscation...")

  pogchampfileformat = file_output.replace(".py", "")

  cmd = "python modules/astobfuscate.py {file_output} {pogchampfileformat}-ast.py".format(
  file_output=file_output,
  pogchampfileformat=pogchampfileformat)
  subprocess.call(cmd, shell=True)

f = open(file_output, "w")
f.write(code)
f.close()

_headers = {"Referer": 'https://rentry.co'}

class UrllibClient:
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
  
def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()

if 6 in layers:
  hash_of_file = (sha256sum(file_output))

  edit(the_stuff[1], the_stuff[2], hash_of_file)

end = time.time()

elapsetime = end-start
print("obfuscation was written to " + file_output)
if do_ast_encrypt == True:
  print("ast last layer written to " + pogchampfileformat + "-ast.py")
print("time to obfuscate: " + str(elapsetime))
