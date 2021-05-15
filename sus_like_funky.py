import random
import base64
import string


# list of one and zero to chose from for the random.choice
# new variable name type
var_type = 3
if var_type == 1:
    whathtenuts = [str(1),str(0)]
elif var_type == 2:
    whathtenuts = ["I", "l"]
elif var_type == 3:
    whathtenuts = ["O", "0"]
else:
    print("Dude.... not a list type available")


code=('''
print("haha lol XD :flushed:")
''')

# V byte code
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


final_script = ("""
watermark = ("Wow this is all it takes to make an 'obfuscator'... sad!")

{hahahahabase} = eval(''.join(chr(int("00111000"[i*8:i*8+8],2)) for i in range(len("00111000")//8)))
{randobj1} = eval(''.join(chr(int("01100101011110000110010101100011"[i*8:i*8+8],2)) for i in range(len("01100101011110000110010101100011")//8)))
{randobj2} = eval(''.join(chr(int("00100111001001110010111001101010011011110110100101101110"[i*8:i*8+8],2)) for i in range(len("00100111001001110010111001101010011011110110100101101110")//8)))
{randobj3} = eval(''.join(chr(int("011000110110100001110010"[i*8:i*8+8],2)) for i in range(len("011000110110100001110010")//8)))
{randobj4} = eval(''.join(chr(int("011010010110111001110100"[i*8:i*8+8],2)) for i in range(len("011010010110111001110100")//8)))
{randobj5} = eval(''.join(chr(int("0111001001100001011011100110011101100101"[i*8:i*8+8],2)) for i in range(len("0111001001100001011011100110011101100101")//8)))
{randobj6} = eval(''.join(chr(int("011011000110010101101110"[i*8:i*8+8],2)) for i in range(len("011011000110010101101110")//8)))
{randobj7} = eval(''.join(chr(int("00110010"[i*8:i*8+8],2)) for i in range(len("00110010")//8)))




{randobj1}({randobj2}({randobj3}({randobj4}(("{res}")[{farted}*{hahahahabase}:{farted}*{hahahahabase}+{hahahahabase}],{randobj7})) for {farted} in {randobj5}({randobj6}(("{res}"))//{hahahahabase})))
""").format(
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

import json
#dud what the fuck am i doing

esketit = {'balls': 'hi_lol', 'dick':{'cock':{'socks': 'fart', 'legodick': 'theexec_code', 'whendidiask':'print("hewwo")'}}}

#fomrat is gonna be like:
#    gen_layer = {'randomtext': 50/50 to either gen another layer or input text}
whathtenuts = [1,0]

letters = string.ascii_lowercase + string.ascii_uppercase
joemama = ( ''.join(random.choice(letters) for i in range(10)) )

def gen_layer(ammount):
    ammount = ammount
    layer=[]
    layers_p_text = []
    #decide = random.choice(whathtenuts)
    for x in range(ammount):
        random_text = ( ''.join(random.choice(letters) for i in range(10)) )
        theform = ("'random_text': {").replace("random_text", random_text)
        layers_p_text.append(random_text)
        layer.append(theform)
    code = ()
    some_text_ig = ("{" + ''.join(layer) + 'exec("""penis_cum""")' +('}' * (ammount+1)))
    print(some_text_ig.replace("penis_cum", final_script))
    

why_dis_no_work = 10
gen_layer(why_dis_no_work)


