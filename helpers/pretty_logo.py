#Honestly i could have made this myself but im to lazy
#pulled from: https://github.com/KasRoudra/k-fuscator/blob/main/kf.py
#purely for the color not even for the code loool
black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"  
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
white="\033[0;37m"

def pretty_logo_func(status):
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
  return(text)


if __name__=="__main__":
  pretty_logo_func()
