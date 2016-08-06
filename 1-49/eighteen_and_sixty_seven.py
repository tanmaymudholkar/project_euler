#!/usr/bin/env python

from __future__ import print_function
from __future__ import division

def initialize(filename):
    global number_of_rows,triangle
    triangle_file=open(filename,'r')
    triangle=[]
    number_of_rows=0
    for array in triangle_file:
        triangle.append([int(number) for number in array.split(' ')])
        number_of_rows=number_of_rows+1

def addtonextrow(row,row_index):
    row_to_return=triangle[row_index+1]
    row_to_return[0] += row[0]
    row_to_return[-1] += row[-1]
    for index_row_to_return in range(1,len(row_to_return)-1):
        row_to_return[index_row_to_return] += max([row[index_row_to_return-1],row[index_row_to_return]])
    return row_to_return

def calculate_max():
    running_sums=triangle[0]
    for row_index in range(0,number_of_rows-1):
        running_sums=addtonextrow(running_sums,row_index)
    return max(running_sums)

if __name__=="__main__":
    initialize("sixty_seven.dat")
    maxsum=calculate_max()
    print ("Maximum sum is %d"%(maxsum))
