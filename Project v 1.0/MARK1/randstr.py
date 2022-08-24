import string
import random

def randstr():
    s=""
    for i in range(5):
        s+=random.choice(string.ascii_letters)
    return s

