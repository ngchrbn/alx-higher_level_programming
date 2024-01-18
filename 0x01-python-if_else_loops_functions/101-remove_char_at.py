#!/usr/bin/python3
def remove_char_at(str, n):
    copied_str = ""
    for i in range(len(str)):
        if i != n:
            copied_str += str[i]
    return copied_str
