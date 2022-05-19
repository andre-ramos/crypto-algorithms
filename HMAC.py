import hashlib


def modify(m):
    l = list(m)
    l[0] = l[0] ^ 2**5
    return bytes(l)

#ALice and Bob share this secret
secret_key = "secret key".encode()

#Alice wants to compute a mac
m = "Hey Bob Whats up".encode()
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = sha256.digest()

print(m, hmac)


#Eve comes along
m = modify(m)
print(m)

#Bob receives and validates the HMAC
ha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = sha256.digest()

print(m, hmac)