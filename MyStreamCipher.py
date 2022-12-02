import random

class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self):
        self.next = (1103515245 * self.next + 12345) % 2 ** 31
        return self.next

    def gen_key_byte(self):
        return self.rand() % 256


# key = KeyStream(20)           #so here we are given the start point (10) so the random # selection start after 10 ,
# so this is the things that we pass to next person as key and due to this we can reuse the key also
# for i in range(10):
# print(key.gen_key_byte())

def encrypt(key, message):
    return bytes([message[i] ^ key.gen_key_byte() for i in range(len(message))])


# with this transmit function we are showing that if some bits in stream cipher lost than the message is still readable
def transmit(cipher, likely):
    b = []
    for c in cipher:
        if random.randrange(0, likely) == 0:
            c = c ^ 2 ** random.randrange(0, 8)
        b.append(c)
    return bytes(b)


# This is Alice
key = KeyStream(10)
message = "Hello World! I am here to declare that I will going to rule this entire empire."
print(message)
message = message.encode()
cipher = encrypt(key, message)
print(cipher)

# This is the poor transmission
cipher = transmit(cipher, 5)

# This is Bob
key = KeyStream(10)
message = encrypt(key, cipher)
print(message)
