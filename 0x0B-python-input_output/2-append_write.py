"""
Appends to a file
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of file and
    returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
