#!/usr/bin/env python

import itertools
import sys

class tri:
    def __init__(self,a):
        self.array=a
        self.srtd=[]
        self.positions=[]
        self.maxlen=[]
        self.length=len(a)
        for i in range(0,len(a)):
            srtd_orig=map(int,sorted(a[i],reverse=True))
            positions_orig=sorted(range(len(a[i])),reverse=True,key=lambda j: a[i][j])
            sameel=[]
            samepos=[]
            sameel_running=[srtd_orig[0]]
            samepos_running=[positions_orig[0]]
            running_element=srtd_orig[0]
            for k in range(1,len(srtd_orig)):
                if(srtd_orig[k]==running_element):
                    sameel_running=sameel_running+[running_element]
                    samepos_running=samepos_running+[positions_orig[k]]
                else:
                    sameel=sameel+[sameel_running]
                    samepos=samepos+[samepos_running]
                    running_element=srtd_orig[k]
                    sameel_running=[srtd_orig[k]]
                    samepos_running=[positions_orig[k]]
            sameel=sameel+[sameel_running]
            samepos=samepos+[samepos_running]
            self.srtd=self.srtd+[sameel]
            self.positions=self.positions+[samepos]
            self.maxlen=self.maxlen+[len(self.srtd[i])]

def read_triangular(tri_file):
    triangle=[]
    for line in tri_file:
        triangle=triangle+[map(int,line.split())]
    tricl=tri(triangle)
    return tricl

def pathburst(putative_pathlist):
    burstlist=[[]]
    for i in range(0,len(putative_pathlist)):
        if(len(putative_pathlist[i])>1):
            prevlen=len(burstlist)
            burstlist=burstlist*len(putative_pathlist[i])
            for j in range(0,len(burstlist)):
                burstlist[j]=burstlist[j]+[putative_pathlist[i][j/prevlen]]
        else:
            for j in range(0,len(burstlist)):
                burstlist[j]=burstlist[j]+[putative_pathlist[i][0]]
    return burstlist        

def enumerate_all_paths(deviation,maxlen,length,positions):
    pathslist=[]
    indices=range(0,length)
    possible_indices=itertools.product(indices,repeat=deviation)
    for possible_index_tuple in possible_indices:
        possible_index_list=list(possible_index_tuple)
        to_be_counted=True
        for i in range(0,deviation-1):
            if possible_index_list[i]>possible_index_list[i+1]:
                to_be_counted=False
                break
        if(to_be_counted):
            path=[0]*length
            for i in possible_index_list:
                if (path[i]+1<maxlen[i]):
                    path[i]=path[i]+1
                else:
                    to_be_counted=False
                    break
        if(to_be_counted):
            putative_pathlist=[]
            for i in range(0,length):
                putative_pathlist=putative_pathlist+[positions[i][path[i]]]
            putative_pathlist_burst=pathburst(putative_pathlist)
            for putative_path in putative_pathlist_burst:
                final_possible=True
                for i in range(0,len(putative_path)-1):
                    if(putative_path[i+1]!=putative_path[i] and putative_path[i+1]!=putative_path[i]+1):
                        final_possible=False
                        break
                if(final_possible):
                    pathslist=pathslist+[putative_path]
    return pathslist

if __name__=='__main__':
    tri_file=open('sixtyseven.dat','r')
    tricl=read_triangular(tri_file)

    tricl_arr=tricl.array
    tricl_srt=tricl.srtd
    tricl_pos=tricl.positions
    tricl_mxl=tricl.maxlen
    tricl_len=tricl.length

    print tricl_srt

    maxdev=0
    for i in range(0,len(tricl_mxl)):
        maxdev=maxdev+tricl_mxl[i]-1

    found=False
    pathslist=[]
    for deviation in range(0,maxdev):
        print "deviation = ",deviation
        pathslist=enumerate_all_paths(deviation,tricl_mxl,tricl_len,tricl_pos)
        if (not pathslist):
            continue
        else:
            break

    max_total=0
    for path in pathslist:
        total=0
        for i in range(0,tricl_len):
            total=total+tricl_arr[i][path[i]]
        if(total>max_total):
            max_total=total

    print "max total is: ",max_total
