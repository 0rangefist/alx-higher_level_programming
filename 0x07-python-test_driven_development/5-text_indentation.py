#!/usr/bin/python3
"""
This module defines text_indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these
    characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # add line breaks after various delimiters
    edited_text = ""
    for char in text:
        edited_text += char
        if char in [".", "?", ":"]:
            edited_text += "\n\n"

    # split the edited text into lines
    lines_of_text = edited_text.splitlines()

    # print trimmed lines (remove leading/trailing spaces)
    for i in range(len(lines_of_text)):
        line = lines_of_text[i].strip()
        print(line.strip(), end="\n" if i < len(lines_of_text) - 1 else "")
