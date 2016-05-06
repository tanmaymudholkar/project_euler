#!/usr/bin/env python

from __future__ import division, print_function

def sum_corners_spiral(n):
    return ((4*n**3 + 3*n**2 + 8*n - 9)//6)

if __name__ == "__main__":
    depth_of_spiral = 1001
    print ("For %i X %i spiral, sum of corners is: %i"%(depth_of_spiral,depth_of_spiral,sum_corners_spiral(depth_of_spiral)))
