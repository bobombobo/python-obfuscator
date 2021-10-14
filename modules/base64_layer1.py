def base64_layer1(code, whathtenuts, dudewhatthenuts):
  import random
  import base64

  # V byte code
  print("base64 encrypting...")
  bc = code.encode('utf-8')
  base64enc=base64.b64encode(bc)

  #gotta use oh's (o) when starting it cuz variables can't use numbers as their first character or something idk


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

  check_for_watermark_yes = ("""exec('''{b64e_run}''')""").format(b64e_run=b64e_run)
  return (check_for_watermark_yes)
