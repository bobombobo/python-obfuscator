def secondarybase64_layer5(nearing_the_end_script):
  import base64
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
  return(dude_im_so_done_with_this)
