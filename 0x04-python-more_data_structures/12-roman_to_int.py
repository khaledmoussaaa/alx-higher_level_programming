#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    ruman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    total = 0
    for i in reversed(roman_string):
        num = ruman[i]
        if total < num * 5:
            total += num
        else:
            num = -num
            total += num
    return total
