def binary_layer2(check_for_watermark_yes, whathtenuts, dudewhatthenuts, variable_ammount_lenght, toup_text_ammount, ammount, top_layers):
  import random


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

  top_text_code = ("""{hahahahabase} = eval(''.join(chr(int("00111000"[i*8:i*8+8],2)) for i in range(len("00111000")//8)));{randobj1} = eval(''.join(chr(int("01100101011110000110010101100011"[i*8:i*8+8],2)) for i in range(len("01100101011110000110010101100011")//8)));{randobj2} = eval(''.join(chr(int("00100111001001110010111001101010011011110110100101101110"[i*8:i*8+8],2)) for i in range(len("00100111001001110010111001101010011011110110100101101110")//8)));{randobj3} = eval(''.join(chr(int("011000110110100001110010"[i*8:i*8+8],2)) for i in range(len("011000110110100001110010")//8)));{randobj4} = eval(''.join(chr(int("011010010110111001110100"[i*8:i*8+8],2)) for i in range(len("011010010110111001110100")//8)));{randobj5} = eval(''.join(chr(int("0111001001100001011011100110011101100101"[i*8:i*8+8],2)) for i in range(len("0111001001100001011011100110011101100101")//8)));{randobj6} = eval(''.join(chr(int("011011000110010101101110"[i*8:i*8+8],2)) for i in range(len("011011000110010101101110")//8)));{randobj7} = eval(''.join(chr(int("00110010"[i*8:i*8+8],2)) for i in range(len("00110010")//8)));""").format(
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
  
  #variable_ammount_lenght = 10
  
  #This one is for how many of the list stuff is for each layer
  
  #toup_text_ammount = 10
  
  #This one is for how many of the list stuff is on top and bottom
  
  #top_layers = 5


  #whathtenuts = [1,0]

  #ammount = 1

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
  return(okay_less_gooooo)
