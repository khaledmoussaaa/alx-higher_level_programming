#!/usr/bin/python3
def uppercase(str):
    for i in word:
        if(ord(i) >= 97 and ord(i) <= 122):
            upper = ord(i) - 32
            print(chr(upper), end="")
        else:
            print(chr(ord(i)), end="")
