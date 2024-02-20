#!/usr/bin/python3
"""
MyInt class defination
"""


class MyInt(int):
    """inherits from class int"""

    def __eq__(self, other):
        """Overrides equals"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Overrides not-equals"""
        return int(self) == int(other)
