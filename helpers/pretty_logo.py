#Honestly i could have made this myself but im to lazy
#pulled from: https://github.com/KasRoudra/k-fuscator/blob/main/kf.py
#purely for the color not even for the code loool
import requests
import os

server_version = requests.get("https://raw.githubusercontent.com/bobombobo/python-obfuscator/main/version.txt").text
#local_version = 
path_parent = os.path.dirname(os. getcwd())
os.chdir(path_parent)
with open((os.getcwd()+"/main.py"), "r") as file:
  content = file.readlines()
  for line in content:
    if server_version in line:
      version_data = ("up-to-date")
      file.close()
      break
  
  version_data = ("outdated")

black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"  
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
white="\033[0;37m"

def pretty_logo_func(status):
  server_version = requests.get("https://raw.githubusercontent.com/bobombobo/python-obfuscator/main/version.txt").text
  #local_version = 
  #path_parent = os.path.dirname(os. getcwd())
  #os.chdir(path_parent)
  with open("main.py", "r") as file:
    content = file.readlines()
    for line in content:
      if server_version in line:
        version_data = ("up-to-date")
        file.close()
        break
      else:
        version_data = ("outdated")
  text=("""
"""+purple+"""██╗░░██╗██████╗░██╗░░░░░██╗░░░░░░█████╗░
"""+blue+  """██║░░██║╚════██╗██║░░░░░██║░░░░░██╔══██╗
"""+cyan+  """███████║░█████╔╝██║░░░░░██║░░░░░██║░░██║
"""+green+ """██╔══██║░╚═══██╗██║░░░░░██║░░░░░██║░░██║
"""+yellow+"""██║░░██║██████╔╝███████╗███████╗╚█████╔╝
"""+red+   """╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝░╚════╝░""")
  if status==("loading"):
    text=text+(purple+"\nloading"+white)

  elif status==("done"):
    text=text+(purple+"\nMad with "+red+"♡"+purple+"  by [" +red+"boboMbobo"+purple+" | "+blue+"https://github.com/bobombobo/"+purple+"]"+cyan+"\nDiscord: "+blue+"https://discord.gg/vJxRgaX2wz"+white+"\n")



    if str(version_data)==("up-to-date"):
      text = text + (cyan +"Version: " + server_version)
    elif version_data==("outdated"):
      text = text+(red +"OLD VERSION! Please conider downloading the latest version\nfor secuirty updates!"+ blue + "\nLatest build " + server_version)
    else:
      text = text+("version check failed")

  return(text)


if __name__=="__main__":
  print(pretty_logo_func("done"))
