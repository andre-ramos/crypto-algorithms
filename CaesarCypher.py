import string

alphabet_list = list(string.ascii_uppercase)

def encrypt(message, shift):
    message_list = list(message)
    cypher_list = []
    for letter in message_list:
        if letter == " ":
            cypher_list.append(" ")
            continue       
        letter_cypher = alphabet_list[(alphabet_list.index(letter) + shift)%26]
        cypher_list.append(letter_cypher)
    return ''.join([str(letter) for letter in cypher_list])

def decrypt(cypher, shift):
    cypher_list = list(cypher)
    message_list = []
    for letter in cypher_list:
        if letter == " ":
            message_list.append(" ")
            continue   
        letter_message = alphabet_list[(alphabet_list.index(letter) - shift)%26]
        message_list.append(letter_message)
    return ''.join([str(letter) for letter in message_list])

    
message = "YOU ARE AWESOME"
shift = 3
cypher = encrypt(message, shift)
print(cypher)
print(decrypt(cypher, shift))
