#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    create = dict()
    for i, j in a_dictionary.items():
        if i == key:
            j = value
        else:
            create[key] = value
    a_dictionary.update(create.items())
    sorted_dict = dict(sorted(a_dictionary.items()))
    for i, j in sorted_dict.items():
        print("{}: {}".format(i, j))
