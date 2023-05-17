#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_dictionary = {"I": 1, "V": 5, "X": 10,
                        "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    prev_numeral = 0
    for key in reversed(roman_string):
        if key in roman_dictionary:
            curr_numeral = roman_dictionary[key]
            if curr_numeral >= prev_numeral:
                result += curr_numeral
            else:
                result -= curr_numeral
            prev_numeral = curr_numeral
        else:
            return 0  # invalid key
    return result
