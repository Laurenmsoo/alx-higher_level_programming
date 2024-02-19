#!/usr/bin/python3
"""
The MyList class module
"""


class MyList(list):
    """MyList class that inherits from list class"""
    def __init__(self):
        """object initialization"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted class"""
        print(sorted(self))
