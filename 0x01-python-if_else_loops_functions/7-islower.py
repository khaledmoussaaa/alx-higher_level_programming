#!/usr/bin/python3
def islower(c):
    for lower in range(ord('a'), ord('z') + 1):
        if(c == chr(lower)):
            return True
    for upper in range(ord('A'), ord('Z') + 1):
        if(c == chr(upper)):
            return False
