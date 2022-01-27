def try_all_imports():
  try:
    import random
  except ModuleNotFoundError:
    cmd = "pip install random"
    subprocess.call(cmd, shell=True,stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    import random

  try:
    import base64
  except ModuleNotFoundError:
    cmd = "pip install base64"
    subprocess.call(cmd, shell=True,stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    import base64

  try:
    import string
  except ModuleNotFoundError:
    cmd = "pip install string"
    subprocess.call(cmd, shell=True,stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    import string

  try:
    import time
  except ModuleNotFoundError:
    cmd = "pip install time"
    subprocess.call(cmd, shell=True,stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    import time

  try:
    import os
  except ModuleNotFoundError:
    cmd = "pip install os"
    subprocess.call(cmd, shell=True,stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    import os

  try:
    import subprocess
  except ModuleNotFoundError:
    cmd = "pip install subprocess"
    subprocess.call(cmd, shell=True,stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    import subprocess

  try:
    import pickle
  except ModuleNotFoundError:
    cmd = "pip install pickle"
    subprocess.call(cmd, shell=True,stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    import pickle
  try:
    #these come from the same package so we can put it into one try statment
    from Crypto.Cipher import PKCS1_OAEP
    from Crypto.PublicKey import RSA
  except ModuleNotFoundError:
    cmd = "pip install pycryptodome"
    subprocess.call(cmd, shell=True,stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    from Crypto.Cipher import PKCS1_OAEP
    from Crypto.PublicKey import RSA

  try:
    import traceback
  except ModuleNotFoundError:
    cmd = "pip install python-minifier"
    subprocess.call(cmd, shell=True,stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    import python_minifier
  try:
    import python_minifier
  except ModuleNotFoundError:
    cmd = "pip install python-minifier"
    subprocess.call(cmd, shell=True,stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    import python_minifier  
  try:
    import time
  except ModuleNotFoundError:
    cmd = "pip install time"
    subprocess.call(cmd, shell=True,stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    import python_minifier 


if __name__=="__main__":
  try_all_imports()
