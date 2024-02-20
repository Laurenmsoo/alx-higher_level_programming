#!/usr/bin/python3
"""
reads file
"""


def read_file(filename=""):
    """reads a and prints it to stdout
    Returns none
    """
    with open(filename, "r", encoding="UTF8") as f:
        print(f.read(), end="")
