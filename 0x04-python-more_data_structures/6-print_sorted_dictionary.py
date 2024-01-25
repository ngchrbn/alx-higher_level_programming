#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.

    Parameters:
    a_dictionary (dict): The dictionary to order.

    Returns:
    None
    """
    sorted_dict = dict(sorted(a_dictionary.items()))

    for key, value in sorted_dict.items():
        print("{}: {}".format(key, value))
