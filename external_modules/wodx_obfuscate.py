import os
import base64
#by wodx :)

def wodx_obfuscate(content, VARIABLE_NAME, OFFSET):
    b64_content = base64.b64encode(content.encode()).decode()
    index = 0
    code = f'{VARIABLE_NAME} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) + 1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{VARIABLE_NAME} += "{_str}"\n'
        index += OFFSET
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
    return code


if __name__=="__main__":
  OFFSET = 10
  VARIABLE_NAME = 'poggers_' * 10
  code=("print('hi')")
  obfuscated = wodx_obfuscate(code, VARIABLE_NAME, OFFSET)
  print(obfuscated)
  exec(obfuscated)