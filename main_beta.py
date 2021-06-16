import random
import base64
import string
import time
import os
import subprocess
import pickle
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import traceback
try:
  import python_minifier
except ModuleNotFoundError:
  cmd = "pip install python-minifier"
  subprocess.call(cmd, shell=True)
  import python_minifier


# !WARNING! ast obfuscation makes the program aprox 150% slower than normal

#2nd base64 encryption is cut into 20 portions, you can change this in line 309

#Options
#------------------------------------------
custom_input = False
custom_output = False
speed_test = False
add_vm_detection_to_script = True
add_vpn_detection_to_script = False #In works :)
use_pickle_serialization = True #May fix "killed" error
minfiy_original_code = False
add_error_encryption = True
#------------------------------------------
#Code
code=('''print("hi!")
print(hi)''')
#------------------------------------------

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

asdf = open("vmcheck_code.txt", "r")
vmcheck_code = (asdf.read())

if custom_input == True:
  print("Select the file to encrypt: ")
  print("Example: code.py, code.txt, ect...")
  file_input = input()
  fopening = open(file_input, "r")
  code = (fopening.read())
else:
  file_input = code


if add_vm_detection_to_script == True:
  code = (vmcheck_code+"\n"+code)
if add_vpn_detection_to_script == True:
  pass

if add_error_encryption == True:
  private_key = RSA.generate(4096)
  public_key = private_key.publickey()
  private_pem = private_key.export_key().decode()
  public_pem = public_key.export_key().decode()
  with open('private_pem.pem', 'w') as pr:
      pr.write(private_pem)
  with open('public_pem.pem', 'w') as pu:
      pu.write(public_pem)
  lessgoo = ('''
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import traceback
try:
  {{code}}
except Exception as ex:
  cipher = PKCS1_OAEP.new(RSA.import_key(open('public_pem.pem', 'r').read()))
  print("You have encountered an error! Send the following message to an administrator to fix it!")
  print("--------------error--------------")
  ex = traceback.format_exc(limit=1)
  message = (str(ex)).encode("utf-8")
  cipher_text = cipher.encrypt(message)
  print(cipher_text)
  print("--------------error--------------")
''').format(code=code)
code = (lessgoo)

if minfiy_original_code==True:
  code = (python_minifier.minify(code))

if custom_output == True:
  file_output = input("Output file: ")
else:
  file_output = ("obfuscated.py")


cls()
start = time.time()

print("Thank you for using my python obfuscator!")
print("Created by boboMbobo | https://github.com/bobombobo")
print("Input: " + file_input)
#print("Output file: " + file_output)
print("--------------------------------------")


# list of one and zero to chose from for the random.choice
# new variable name type
var_type = 1
if var_type == 1:
    whathtenuts = [str(1),str(0)]
elif var_type == 2:
    whathtenuts = ["I", "l"]
elif var_type == 3:
    whathtenuts = ["O", "0"]
else:
    print("Dude.... not a list type available")



# V byte code
print("base64 encrypting...")
bc = code.encode('utf-8')
base64enc=base64.b64encode(bc)

#gotta use oh's (o) when starting it cuz variables can't use numbers as their first character or something idk
dudewhatthenuts = "nil"
if var_type == 1 or var_type == 3:
    dudewhatthenuts = "O"
else:
    dudewhatthenuts = ""

bruhlol = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(12)))
bruhlol2 = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(12)))
bruhlol3 = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(12)))
lessgoo = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(12)))

b64e_run = ("""
import base64
{bruhlol} = {base64enc}
{bruhlol2} = base64.b64decode({bruhlol})
{bruhlol3} = {bruhlol2}.decode('utf-8')
exec({bruhlol3})
""").format(
base64enc=base64enc,
bruhlol=bruhlol,
bruhlol2 = bruhlol2,
bruhlol3=bruhlol3,
lessgoo=lessgoo,
)

check_for_watermark_yes = ("""
if watermark == ("Wow this is all it takes to make an 'obfuscator'... sad!"):
  exec('''{b64e_run}''')
""").format(b64e_run=b64e_run)

print("binary encrypting...")

res = ''.join(format(ord(i), '08b') for i in check_for_watermark_yes)

farted = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(12)))
hahahahabase = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(12)))
randobj1 = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(12)))
randobj2 = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(12)))
randobj3 = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(12)))
randobj4 = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(12)))
randobj5 = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(12)))
randobj6 = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(12)))
randobj7 = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(12)))

top_text_code = ("""watermark = ("Wow this is all it takes to make an 'obfuscator'... sad!");{hahahahabase} = eval(''.join(chr(int("00111000"[i*8:i*8+8],2)) for i in range(len("00111000")//8)));{randobj1} = eval(''.join(chr(int("01100101011110000110010101100011"[i*8:i*8+8],2)) for i in range(len("01100101011110000110010101100011")//8)));{randobj2} = eval(''.join(chr(int("00100111001001110010111001101010011011110110100101101110"[i*8:i*8+8],2)) for i in range(len("00100111001001110010111001101010011011110110100101101110")//8)));{randobj3} = eval(''.join(chr(int("011000110110100001110010"[i*8:i*8+8],2)) for i in range(len("011000110110100001110010")//8)));{randobj4} = eval(''.join(chr(int("011010010110111001110100"[i*8:i*8+8],2)) for i in range(len("011010010110111001110100")//8)));{randobj5} = eval(''.join(chr(int("0111001001100001011011100110011101100101"[i*8:i*8+8],2)) for i in range(len("0111001001100001011011100110011101100101")//8)));{randobj6} = eval(''.join(chr(int("011011000110010101101110"[i*8:i*8+8],2)) for i in range(len("011011000110010101101110")//8)));{randobj7} = eval(''.join(chr(int("00110010"[i*8:i*8+8],2)) for i in range(len("00110010")//8)));""").format(
res=res,
hahahahabase=hahahahabase, 
farted=farted, 
randobj1=randobj1, 
randobj2=randobj2,
randobj3=randobj3,
randobj4=randobj4,
randobj5=randobj5,
randobj6=randobj6,
randobj7=randobj7)


final_script = ("""{randobj1}({randobj2}({randobj3}({randobj4}(("{res}")[{farted}*{hahahahabase}:{farted}*{hahahahabase}+{hahahahabase}],{randobj7})) for {farted} in {randobj5}({randobj6}(("{res}"))//{hahahahabase})))""").format(
res=res,
hahahahabase=hahahahabase, 
farted=farted, 
randobj1=randobj1, 
randobj2=randobj2,
randobj3=randobj3,
randobj4=randobj4,
randobj5=randobj5,
randobj6=randobj6,
randobj7=randobj7)

#print(final_script)

#res = ''.join(chr(int(res[i*8:i*8+8],2)) for i in range(len(res)//8))

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
#JSON obfuscation? idk man im bored
#dud what the fuck am i doing

#lets define some choices
#okay i guess ill tell you what each variable does cuz idk any more :)
#This one is for how long each lenght of characters is for the string of the stuff
#ex: variable_ammount_lenght = 10 so in {'O0001011110':, the lenght is 10 or something
variable_ammount_lenght = 10
#This one is for how many of the list stuff is for each layer
toup_text_ammount = 10
#This one is for how many of the list stuff is on top and bottom
top_layers = 5


#whathtenuts = [1,0]

ammount = 1

#This one is to form the string where the code is embeded :)
print("list encrypting...")

layer=[]
layers_p_text = []
#decide = random.choice(whathtenuts)
for x in range(ammount):
    random_text = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(variable_ammount_lenght)))
    theform = ("'random_text': {").replace("random_text", random_text)
    layers_p_text.append(random_text)
    layer.append(theform)


#This one doesnt do shit i guess
"""
back_at_it = []
back_p_text = []
for x in range(ammount):
    random_text = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(variable_ammount_lenght)))
    theform = ("'random_text': {").replace("random_text", random_text)
    back_p_text.append(random_text)
    back_at_it.append(theform)
  """ 
    
some_text_ig = ("{" + ''.join(layer) + 'penis_cum' + ('}' * (ammount+1)))

#just using random names now cuz i don't want to name anymore
#What the fuck does this do????????
#OOOHHH it prints the water mark and definitions of functions
#changed place for another layer :)

#Okay this one is the top layers of random strings
for x in range(top_layers): #this many interations on the bottom
    urwpu13948h5 = []
    asd908ugunwqing = []
    #toup_text_ammount = 2 #12 line on top of the actual code text
    for x in range(toup_text_ammount):
        random_text = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(variable_ammount_lenght)))
        theform = ("'random_text': {").replace("random_text", random_text)
        urwpu13948h5.append(random_text)
        asd908ugunwqing.append(theform)
    
    ueapiogwh = ("{" + ''.join(asd908ugunwqing) + ('}' * (toup_text_ammount+1)))


#This creates the actual script to be executed 
dickfuck = (some_text_ig.replace("penis_cum", final_script))

#and then this one is thebottom layers of random strings
for x in range(top_layers): #this many interations on bottom
    urwpu13948h5 = []
    asd908ugunwqing = []
    #toup_text_ammount = 2 #12 line on top of the actual cod text
    for x in range(toup_text_ammount):
        random_text = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(variable_ammount_lenght)))
        theform = ("'random_text': {").replace("random_text", random_text)
        urwpu13948h5.append(random_text)
        asd908ugunwqing.append(theform)
    
    okayLesGo = ("{" + ''.join(asd908ugunwqing) + ('}' * (toup_text_ammount+1)))

print("i-1 encrypting...")

okay_less_gooooo = ("""
{top_text_code}
{ueapiogwh}
{dickfuck}
{okayLesGo}
""").format(
top_text_code=top_text_code,
ueapiogwh=ueapiogwh,
dickfuck=dickfuck,
okayLesGo=okayLesGo
)

uwgahpoiuhgwiuagb = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(12)))


gheawiuhgauwieg = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(12)))

awengjanwe = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(12)))
epwiuahgiaw = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(12)))
eiawhgiuedbvg = dudewhatthenuts+(''.join(random.choice(whathtenuts) for i in range(12)))

def encrypt(string):
    split_string = list(string)
    end_string = []
    for x in range(len(split_string)):
        end_string.append(str((ord(split_string[x]))*"I"))

    end2 = 'llllllllllllllll'.join(end_string)
    return(end2)

pogchamp = encrypt(okay_less_gooooo)
#print("Combining strings...")
reformated = ("""{uwgahpoiuhgwiuagb} = ('{pogchamp}');""").format(pogchamp=pogchamp,
uwgahpoiuhgwiuagb=uwgahpoiuhgwiuagb)

bottom_text_ipuahwpeg = ("""
{epwiuahgiaw} = {uwgahpoiuhgwiuagb}.split("llllllllllllllll");{gheawiuhgauwieg} = [];
for x in range(len({epwiuahgiaw})):
  {eiawhgiuedbvg} = (len({epwiuahgiaw}[x]));{gheawiuhgauwieg}.append(chr({eiawhgiuedbvg})) 
{awengjanwe} = ''.join({gheawiuhgauwieg});exec({awengjanwe})""").format(
uwgahpoiuhgwiuagb=uwgahpoiuhgwiuagb,
awengjanwe=awengjanwe,
gheawiuhgauwieg=gheawiuhgauwieg,
epwiuahgiaw=epwiuahgiaw,
eiawhgiuedbvg=eiawhgiuedbvg
)

nearing_the_end_script = (reformated + bottom_text_ipuahwpeg)


#f = open(file_output, "w")
#f.write(nearing_the_end_script)
#f.close()

print("Secondary base64 encrypting")

joe = (nearing_the_end_script)
spliting = joe.encode('utf-8')
spliting = base64.b64encode(spliting)
spliting = spliting.decode('utf-8')
split_strings = []
n  = int((len(spliting))/20)
for index in range(0, len(spliting), n):
    split_strings.append(spliting[index : index + n])

lmaooo = ('"'+ '"+"'.join(split_strings) + '"')
dude_im_so_done_with_this = '''import base64;exec((base64.b64decode(({lmaooo}).encode('utf-8'))).decode('utf-8'))'''.format(lmaooo=lmaooo)


if use_pickle_serialization==True:
  print("Pickle serialization encrypting...")

  string_list = list(dude_im_so_done_with_this)
  pickle_dump = pickle.dumps(string_list)

  #dude_im_so_done_with_this = ("""import pickle;pickle_dump = {pickle_dump};exec(''.join(pickle.loads(pickle_dump)))""").format(pickle_dump=pickle_dump)

  dude_im_so_done_with_this = ("""import pickle;exec(''.join(pickle.loads({pickle_dump})))""").format(pickle_dump=pickle_dump)

f = open(file_output, "w")
f.write(dude_im_so_done_with_this)
f.close()

print("Starting secondary ast obfuscation...")

pogchampfileformat = file_output.replace(".py", "")

cmd = "python ASTObfuscate/astobfuscate.py {file_output} {pogchampfileformat}-ast.py".format(
file_output=file_output,
pogchampfileformat=pogchampfileformat
)

subprocess.call(cmd, shell=True)

end = time.time()
elapsetime = end-start
print("normal written to " + file_output)
print("ast last layer written to " + pogchampfileformat + "-ast.py")
print("time to obfuscate: " + str(elapsetime))


if speed_test == True:
  print("Test one...")
  cmd = "python obfuscated.py"
  start = time.time()
  subprocess.call(cmd, shell=True)
  end = time.time()
  elapse1 = (end-start)
  print("Test two...")
  cmd = "python obfuscated-ast.py"
  start = time.time()
  subprocess.call(cmd, shell=True)
  end = time.time()
  elapse2 = (end-start)
  how_much_faster_1_is_than_2 = (elapse1-elapse2)
  print("Speed difference: "+str(int((elapse1/elapse2)*100)) + "%")
