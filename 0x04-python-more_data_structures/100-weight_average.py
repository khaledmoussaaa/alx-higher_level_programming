#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    score = 1
    weight = 0
    average = 0
    new_list = []
    for i in my_list:
        for j in range(len(i)):
            score = score * i[j]
            if j == 1:
                weight = weight + i[j]
        new_list.append(score)
        score = 1
    return (sum(new_list) / weight)
