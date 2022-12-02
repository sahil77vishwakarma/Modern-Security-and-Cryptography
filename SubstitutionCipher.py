import random


def generate_key():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cletter = list(letters)
    key = {}

    for c in letters:
        key[c] = cletter.pop(random.randint(0, len(cletter) - 1))
    return key

def get_decryption_key(key):
    dkey = {}
    for c in key:
        dkey[key[c]] = c
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
dkey = get_decryption_key(key)
message = encrypt(dkey, cipher)
print(message)
