#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first_char = None
        my_tuple = (length, first_char)
        return my_tuple
    else:
        first_char = sentence[0]
        my_tuple = (length, first_char)
        return my_tuple
