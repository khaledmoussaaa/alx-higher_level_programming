#!/usr/bin/python3
def uppercase(str):
    store = ''
    for i in str:
        upper = ord(i)
        if(ord(i) >= 97 and ord(i) <= 122):
            upper = ord(i) - 32
            store = store + chr(upper)
        else:
            store = store + chr(ord(i))
    print("{}".format(store))
