# JOIN THE DISCORD!!!!!!!
https://discord.gg/2HCX5Dqhsq

# python-obfuscator
different obfuscator/encryptions methods made by me and some from others in the comunnity.

Obfuscate your python code to make it almost impsossible to read but a computer can still understand it without a flaw.

(Sorry for shit documentation and horrible commenting. Also sorry for the terrible variable names lol :)

# Update V2.4
Added Kramer obfuscation method as an external module (#3) (https://github.com/billythegoat356/Kramer)

Added a version check t ocheck version of repo and client version.

# V2 RELEASE! Info:

V2 comes built with modules instead of using one big file, so the code can be expanded and even you can create your own modules for expansion!

V2 also comes in with other built in tools! Such as error encrypting and VM detection. All of which can be modified to your taste!

# Options! (and the meaning of each one)

Each option of the obfuscator is used for a purpose, here I will tell you what they mean and what they do.

Layers:
  - Layer 1: This layer is for the first iteration of base64 encoding.
  - Layer 2: This is 2 layers in one, it is a combination of binary encryption and list encrypting.
  - Layer 3: Layer 3 is splitting of the code with 1's and i's.
  - Layer 4: Secondary base64 encryption this time with a different method 
  - Layer 5: Pickle serialization so it can't be read by a human.
  - Layer 6: Pickle serialization for no-tamper exploitation. When unserialized the code is ran to check if someone has tampered with the code
External Layers:
  - Layer 1: py_fuscate method
  - Layer 2: wodx_obfuscate method
  - Layer 3: kramer method

custom_input (True/False): If True a custom input of a file will be needed to then be imported as code. If False a varaible will be used to determine the code to obfuscate. 

custom_output (True/False): If True the output of the encrypted file will be output as what you set it to. If false the code will be exported as "obfuscated.py" and rewrite any other "obfuscated.py" that was there (if any).

speed_test (True/False): If true your code will be ran with subproccess.call to test speed difference in normal obfuscation vs ast obfsucation. (Wonky and really weird I really just used this to debug stuff)

add_vm_detection_to_script (True/False): This will add the vm detection to your code at the very top of it. Learn more about the code in vmcheck_code.txt.

minify_original_code (True/False): This will use python minifier to make your code smaller. This could be considered a obfuscation tenique as well.

add_error_encryption (True/False): This will add error encryption to your program, you will get a private_key.pem to use to decrypt errors. If your program encounters an error the end user will not be able to see the error. (Use error_decoder.py to decode errors so you can see what the error is)

do_ast_encrypt (True/False): This will try to do the ast encryption making your code lots safer, but making it quite a bit slower. It's very buggy fyi.

var_type (1, 2, and 3): This will determine how you want your names/patterns of the variables used. 
1=1,0
2=I,1
3=O,0


