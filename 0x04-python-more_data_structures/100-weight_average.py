#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple (<score>, <weight>)"""
    if not my_list:
        return 0

    total_weight = 0
    total_value = 0

    for score, weight in my_list:
        total_weight += weight
        total_value += score * weight

    return total_value / total_weight
