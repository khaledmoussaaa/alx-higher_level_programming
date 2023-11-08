#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    best_score = ''
    for i in a_dictionary.keys():
       if max < a_dictionary[i]:
           max = a_dictionary[i]
           best_score = i
    return best_score
