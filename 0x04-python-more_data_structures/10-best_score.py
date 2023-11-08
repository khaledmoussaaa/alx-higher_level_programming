#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = 0
    best_score = ''
    for i, j in a_dictionary.items():
        if max < j:
            max = j
            best_score = i
    return best_score
