from tryImports import *
try_all_imports()
import time
import subprocess
from modules.errorencrypt import *
from modules.base64_layer1 import *
from modules.binary_layer2 import *
from modules.split_layer4 import *
from modules.secondarybase64_layer5 import *
from modules.pickle_layer6 import *

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

#options :)
layers = [1,2,3,4,5]

custom_input = False
custom_output = False
speed_test = False
add_vm_detection_to_script = False
use_pickle_serialization = True #May fix "killed" error
minfiy_original_code = False
add_error_encryption = True
do_ast_encrypt = False
var_type = 1



#end of options

#code unless custom input :) used for testing mainly
code=('''
print("hi!")''')

if minfiy_original_code==True:
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


print("Thank you for using my python obfuscator!")
print("Created by boboMbobo | https://github.com/bobombobo")
print("Input: " + file_input)
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


code = errorencryptcode(code)

if 1 in layers:
  code = base64_layer1(code, whathtenuts, dudewhatthenuts)

#Check in the module file to see what the numbers doe and such. I explain it there 
#variable_ammount_lenght, toup_text_ammount, ammount, top_layers
if 2 in layers:
  code = binary_layer2(code, whathtenuts, dudewhatthenuts,10, 10, 1, 5)

#code = list_layer3(code, whathtenuts, dudewhatthenuts, top_text_code)
if 3 in layers:
  code = split_layer4(code, whathtenuts, dudewhatthenuts)

if 4 in layers:
  code = secondarybase64_layer5(code)
if 5 in layers:
  code = pickle_layer6(code)

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

end = time.time()
elapsetime = end-start
print("normal written to " + file_output)
if do_ast_encrypt == True:
  print("ast last layer written to " + pogchampfileformat + "-ast.py")
print("time to obfuscate: " + str(elapsetime))
