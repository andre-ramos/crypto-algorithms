from pyDes import *


def modify_many_bits(cipher):
    mod = [0]*len(cipher)
    print("Mod: "+str(mod))
    mod[10] = ord(' ') ^ ord('1')
    mod[11] = ord(' ') ^ ord('0')
    mod[12] = ord('1') ^ ord('0')
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])

def modify(cipher):
    mod = [0]*len(cipher)
    print("Mod: "+str(mod))
    mod[8] = 1
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])

message = "Give Bob       10$"
key = "DESCRYPT"
iv = bytes([0]*8)
# create the cipher here
k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)

cipher = k.encrypt(message)
# Alice sending the encrypted message
# encrypt the message to cipher
print("Length of plain text:", len(message))
print("Length of cipher text:", len(cipher))
print("Encrypted:", cipher)


# Bob decrypting the cipher text
cipher = modify(cipher)

# decrypt the cipher to message
message = k.decrypt(cipher)
print("Decrypted:", message)
