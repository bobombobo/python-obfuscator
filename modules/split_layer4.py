import random
def split_layer4(okay_less_gooooo, whathtenuts, dudewhatthenuts):
  print("Splitting encrypting")
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
  return(nearing_the_end_script)
