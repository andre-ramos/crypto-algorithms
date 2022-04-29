import random


class KeyStream:
    def __init__(self, key=1) -> None:
        self.next = key

    def rand(self):
        self.next = (1103515245*self.next + 12345) % 2**31
        return self.next
    
    def get_key_byte(self):
        return self.rand() % 256

def encrypt(key, message):
    return bytes([message[i] ^key.get_key_byte() for i in range(len(message))])

# Implementing transmit failure possibility
def transmit(cipher, likely):
    b = []
    for c in cipher:
        if random.randrange(0, likely) == 0:
            c = c ^ 2**random.randrange(0, 8)
        b.append(c)
    return bytes(b)

# Transmitting exercise
#flip the 6th least significant bit of the 4th byte
def transmit_(cipher):
    # insert code here
    b = []
    a = 0
    for c in cipher:
        if a == 3:
            c = (c ^ 32)
        b.append(c)
        a = a + 1
    return bytes(b)

# if somebody modify the message
def modification(cipher):
    mod = [0]*len(cipher)
    mod[10] = ord(' ') ^ ord('1')
    mod[11] = ord(' ') ^ ord('0')
    mod[12] = ord('0') ^ ord('1')
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])


key = KeyStream(10)
message = "Send Bob:   10$".encode()
cipher = encrypt(key, message)
print(cipher)

# cipher = transmit_(cipher)
# This is Bob modifying the message
cipher = modification(cipher)

key = KeyStream(10)
message = encrypt(key, cipher)
print(message)