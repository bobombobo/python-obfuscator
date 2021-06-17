def pickle_layer6(dude_im_so_done_with_this):
  import pickle
  print("pickel encrypting")
  string_list = list(dude_im_so_done_with_this)
  pickle_dump = pickle.dumps(string_list)

  #dude_im_so_done_with_this = ("""import pickle;pickle_dump = {pickle_dump};exec(''.join(pickle.loads(pickle_dump)))""").format(pickle_dump=pickle_dump)

  dude_im_so_done_with_this = ("""import pickle;exec(''.join(pickle.loads({pickle_dump})))""").format(pickle_dump=pickle_dump)
  return(dude_im_so_done_with_this)
