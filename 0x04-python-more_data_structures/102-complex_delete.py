#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary.

    Parameters:
    a_dictionary (dict): The dictionary to modify.
    value: The value to delete keys for.

    Returns:
    dict: The modified dictionary.
    """
    for key in list(a_dictionary.keys()):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
