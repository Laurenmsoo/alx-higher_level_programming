#!/usr/bin/python3
"""append_after function defination."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file.
    Args:
        filename (str): The name of the file.
        search_string (str): The string to search
        new_string (str): The string to append.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as f:
        f.write(text)
