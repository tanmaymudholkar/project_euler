#!/usr/bin/env python

from __future__ import print_function, division

mapping={chr(n):1+n-ord('A') for n in range(ord('A'),1+ord('Z'))}

def initialize():
    global list_of_names
    list_of_names = []
    with open(filename) as file_containing_list_of_names:
        line = file_containing_list_of_names.readline()
        list_of_names.extend([name.strip("\"") for name in line.split(",")])
    list_of_names.sort()

def score(name):
    name_score = 0
    for character in name:
        name_score += mapping[character]
    return name_score

def total_score():
    list_total_score = 0
    for position_name in range(1,1+len(list_of_names)):
        list_total_score += position_name*score(list_of_names[position_name-1])
    return list_total_score

if __name__ == "__main__":
    filename="p022_names.txt"
    initialize();
    required_score=total_score()
    print ("Required score is %d"%(required_score))
