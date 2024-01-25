#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        highest = list(a_dictionary.keys())[0]
        for i in a_dictionary.keys():
            if a_dictionary[i] > a_dictionary.get(highest):
                highest = i
        return highest
