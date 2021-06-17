from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
def errorencryptcode(code):
  private_key = RSA.generate(4096)
  public_key = private_key.publickey()
  private_pem = private_key.export_key().decode()
  public_pem = public_key.export_key().decode()
  with open('private_pem.pem', 'w') as pr:
      pr.write(private_pem)
  with open('public_pem.pem', 'w') as pu:
      pu.write(public_pem)
  code=code
  lessgoo = ('''
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import traceback
try:
  exec("""{code}""")
except Exception as ex:
  cipher = PKCS1_OAEP.new(RSA.import_key(open('public_pem.pem', 'r').read()))
  print("You have encountered an error! Send the following message to an administrator to fix it!")
  print("--------------error--------------")
  ex = traceback.format_exc(limit=1)
  message = (str(ex)).encode("utf-8")
  cipher_text = cipher.encrypt(message)
  print(cipher_text)
  print("--------------error--------------")
  ''').format(code=code)
  return(lessgoo)
