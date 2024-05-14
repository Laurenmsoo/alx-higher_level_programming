#!/usr/bin/python3
"""Integer list algs."""


def find_peak(integersl):
    """checks for the peak in a list of unsorted integers."""
    if integersl:
        integersl.sort(reverse=True)
        return integersl[0]
