#pulled from
#https://github.com/Sl-Sanda-Ru/Py-Fuscate/blob/main/py_fuscate.py

import subprocess
import pickle
import os
import marshal
import os
import sys
import random
import lzma
import gzip
import bz2
import binascii
import zlib




def marsh_enc(code):
    sel_cyph = random.choice((lzma, gzip, bz2, binascii, zlib))
    source_marshal = marshal.dumps(compile(code, 'obfuscated', 'exec'))
    if sel_cyph is binascii:
        cyph_compressed = binascii.b2a_base64(source_marshal)
    else:
        cyph_compressed = sel_cyph.compress(source_marshal)
    if sel_cyph is binascii:
        return 'import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(binascii.a2b_base64(%s)))'%cyph_compressed
    else:
        return 'import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(%s.decompress(%s)))'%(sel_cyph.__name__, cyph_compressed)


if __name__=="__main__":
  for x in range(10):
    code = marsh_enc(code)

  print(code)
  exec(code)
