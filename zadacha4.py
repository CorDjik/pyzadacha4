alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


# def print_chastota(msg):
#    col = [sum([1 for letter1 in msg if letter1 == letter2]) for letter2 in alphabet]
#    total = sum(col)
#    for i, l in enumerate(alphabet):
#        print(l, round(col[i] / total, 4))
def print_chastota(msg):
    for letter2 in alphabet:
        print(
            letter2,
            round(sum([1 for letter1 in msg if letter1 == letter2]) / len(msg), 4),
        )


# with open("key.txt") as f1:
#    key = f1.read().lower()
# with open("msg.txt") as f2:
#    msg = f2.read().lower()

# key_ = ""
# for i in range(len(key)):
#    if key[i] in alphabet:
#        key_ += key[i]
# msg_ = ""
# for i in range(len(msg)):
#    if msg[i] in alphabet:
#        msg_ += msg[i]
with open("key.txt") as f1:
    key = "".join(a for a in f1.read().lower() if a in alphabet)
with open("msg.txt") as f2:
    msg = "".join(a for a in f2.read().lower() if a in alphabet)

print_chastota(msg)

import math

# key_ = key_ * math.ceil(len(msg_) / len(key_))
# new_msg = ""
# for i in range(len(msg_)):
#    new_msg += alphabet[
#        (alphabet.find(msg_[i]) + alphabet.find(key_[i])) % len(alphabet)
#    ]
key = key * math.ceil(len(msg) / len(key))
new_msg = "".join(
    alphabet[(alphabet.find(msg[i]) + alphabet.find(key[i])) % len(alphabet)]
    for i in range(len(msg))
)

print(new_msg)
print_chastota(new_msg)
