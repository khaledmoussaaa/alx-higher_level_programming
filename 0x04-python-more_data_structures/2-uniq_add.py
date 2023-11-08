#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    sum = 0
    for i in my_list:
        my_set.add(i)
    for i in my_set:
        sum += i
    return sum
