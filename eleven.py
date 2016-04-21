#!/usr/bin/env python
import numpy
import math

data_from_file=numpy.loadtxt('eleven.dat',dtype=int,comments='#')

running_max=0

#horizontal
for i in range(0,17):
    for j in range(0,20):
        product=data_from_file[i,j]*data_from_file[i+1,j]*data_from_file[i+2,j]*data_from_file[i+3,j]
        if(product>running_max):
            running_max=product

#vertical
for i in range(0,20):
    for j in range(0,17):
        product=data_from_file[i,j]*data_from_file[i,j+1]*data_from_file[i,j+2]*data_from_file[i,j+3]
        if(product>running_max):
            running_max=product

#top left to bottom right
for i in range(0,17):
    for j in range(0,17):
        product=data_from_file[i,j]*data_from_file[i+1,j+1]*data_from_file[i+2,j+2]*data_from_file[i+3,j+3]
        if(product>running_max):
            running_max=product

#top right to bottom left
for i in reversed(range(3,20)):
    for j in range(0,17):
        product=data_from_file[i,j]*data_from_file[i-1,j+1]*data_from_file[i-2,j+2]*data_from_file[i-3,j+3]
        if(product>running_max):
            running_max=product

print running_max
