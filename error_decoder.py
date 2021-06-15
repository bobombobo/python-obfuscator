#decypher program
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import traceback

message = (replace here with error message)

decrypt = PKCS1_OAEP.new(RSA.import_key(open('private_pem.pem', 'r').read()))
decrypted_message = decrypt.decrypt(message)
print(decrypted_message.decode("utf-8"))
