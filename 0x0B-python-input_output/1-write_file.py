#!/usr/bin/python3
"""
write a file
"""


def write_file(filename="", text=""):
    """
    write a string to a file and returns the number
    of characters writen
    """
    with open(filename, "w", encoding="UTF8") as f:
        return f.write(text)
