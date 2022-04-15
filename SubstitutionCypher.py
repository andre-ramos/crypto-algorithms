from email import message
from random import random
import string
import random

def generate_key():
    letters = alphabet_list = list(string.ascii_uppercase)
    cletters = list(letters)
    key = {}
    for c in letters:
        key[c] = cletters.pop(random.randint(0, len(cletters) - 1))
    return key

def get_decrypt_key(key):
    dkey = {}
    for k in key:
        dkey[key[k]] = k
    return dkey

def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
                cipher += c
    return cipher


key = generate_key()
print(key)
message = "YOU ARE AWESOME"
cipher = encrypt(key, message)
print(cipher)
dkey = get_decrypt_key(key)
message = encrypt(dkey, cipher)
print(message)