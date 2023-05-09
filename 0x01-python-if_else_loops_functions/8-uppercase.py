#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    # check if a char in str is lowercase
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            # convert it to upper case
            upper_str += chr(ord(char) - 32)
        else:
            upper_str += char
    print("{}".format(upper_str))
