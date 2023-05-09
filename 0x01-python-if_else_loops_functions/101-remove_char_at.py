#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    str_cpy = ""
    for i in range(0, len(str)):
        if i != n:
            str_cpy += str[i]
    return str_cpy
