#!/usr/bin/env python

import math
import numpy

def get_list_of_indices(element,array):
    match_list=[]
    for putative_match in array:
        if(element==putative_match):
            match_list.append(putative_match)
    return match_list

triangle_file=open('eighteen.dat','r')

triangle=[]

for array in triangle_file:
    triangle.append([int(number) for number in array.split(' ')])

sorted_triangle=[]
for row in triangle:
    sorted_triangle.append(sorted(row,reverse=True))

index_list=[]
for sorted_row in sorted_triangle:
    index_list_row=[get_list_of_indices(sorted_row[0],sorted_row)]
    last_element_for_which_index_created=sorted_row[0]
    for element in sorted_row[1:]:
        if (element==last_element_for_which_index_created):
            continue
        else:
            index_list_row.append(get_list_of_indices(element,sorted_row))
            last_element_for_which_index_created=element
    index_list.append(index_list_row)

print triangle
print sorted_triangle
print index_list
