#!/usr/bin/env python

#import itertools
#import sys
import cProfile
#import math

#divisions_list=[]

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

def divisions_of_n(n,*mne_inp):
    mne=list(mne_inp)
    if (not mne):
        return divisions_of_n(n,n)
    else:
        must_not_exceed=mne[0]
        if(must_not_exceed<1 or n<1):
            return []
        elif(n==1 and (must_not_exceed==1 or must_not_exceed>1)):
            return [[1]]
        elif(must_not_exceed==1 and (n==1 or n>1)):
            return [[1]*n]
        else:
            divisions=[]
            if(must_not_exceed>n or must_not_exceed==n):
                divisions=[[n]]
            for i in range(max(1,(n-must_not_exceed)),n):
                must_not_exceed_new=n-i
                toadd_right_array=divisions_of_n(i,must_not_exceed_new)
                toadd_left=[n-i]
                for toadd_right in toadd_right_array:
                    division=list(toadd_left)
                    division.extend(toadd_right)
                    if(not divisions):
                        divisions=[division]
                    else:
                        divisions.append(division)
            return divisions

def pathburst(putative_pathlist):
    burstlist=[[]]
    for i in range(0,len(putative_pathlist)):
        prevlen=len(burstlist)
        burstlist=burstlist*len(putative_pathlist[i])
        for j in range(0,len(burstlist)):
            burstlist[j]=burstlist[j]+[putative_pathlist[i][j/prevlen]]
    return burstlist

def unique_perms(revsorted_a):
    if(not revsorted_a):
        return []
    elif (len(revsorted_a)==1):
        return [revsorted_a]
    else:
        sameel=[]
        sameel_running=[revsorted_a[0]]
        samepos_running_counter=1
        running_element=revsorted_a[0]
        for j in range(1,len(revsorted_a)):
            if(revsorted_a[j]==running_element):
                samepos_running=samepos_running+[positions[j]]
            else:
                sameel=sameel+[sameel_running]
                samepos=samepos+[samepos_running]
                running_element=revsorted_a[j]
                sameel_running=[revsorted_a[j]]
                samepos_running=[positions[j]]
        sameel=sameel+[sameel_running]
        samepos=samepos+[samepos_running]
        
    

# def enumerate_all_paths(deviation,maxlen,length,positions):
#     #pathslist=[]
#     divisions=divisions_of_n(deviation)
#     if (not(not(divisions))):
#         for division in divisions:
#             if(len(division)<=length):
#                 number_of_zeros_to_fill=length-len(division)
#                 division.append([0]*number_of_zeros_to_fill)
#                 possible_index_list=unique_permutations(division)
#                 for path in possible_paths:
#                     permutations=unique_perms(path,maxlen,length)
#                     for permutation in permutations:
#     else:
#         yield [[0]*length]

# POSSIBLY WORKING?
# def enumerate_all_paths(deviation,maxlen,length,positions):
#     pathslist=[]
#     indices=range(0,length)
#     possible_indices=itertools.product(indices,repeat=deviation)
#     for possible_index_tuple in possible_indices:
#         possible_index_list=list(possible_index_tuple)
#         to_be_counted=True
#         for i in range(0,deviation-1):
#             if possible_index_list[i]>possible_index_list[i+1]:
#                 to_be_counted=False
#                 break
#         if(to_be_counted):
#             path=[0]*length
#             for i in possible_index_list:
#                 if (path[i]+1<maxlen[i]):
#                     path[i]=path[i]+1
#                 else:
#                     to_be_counted=False
#                     break
#         if(to_be_counted):
#             putative_pathlist=[]
#             for i in range(0,length):
#                 putative_pathlist=putative_pathlist+[positions[i][path[i]]]
#             putative_pathlist_burst=pathburst(putative_pathlist)
#             for putative_path in putative_pathlist_burst:
#                 final_possible=True
#                 for i in range(0,len(putative_path)-1):
#                     if(putative_path[i+1]!=putative_path[i] and putative_path[i+1]!=putative_path[i]+1):
#                         final_possible=False
#                         break
#                 if(final_possible):
#                     pathslist=pathslist+[putative_path]
#     return pathslist

def getmax(tri_file_name):
    tri_file=open(tri_file_name,'r')
    tricl=read_triangular(tri_file)

    tricl_arr=tricl.array
    tricl_srt=tricl.srtd
    tricl_pos=tricl.positions
    tricl_mxl=tricl.maxlen
    tricl_len=tricl.length

    maxdev=0
    for i in range(0,len(tricl_mxl)):
        maxdev=maxdev+tricl_mxl[i]-1

    found=False
    pathslist=[]
    counter=0
    for deviation in range(0,maxdev):
        print "deviation = ",deviation
        pathslist=enumerate_all_paths(deviation,tricl_mxl,tricl_len,tricl_pos)
        print "number of paths = ",len(pathslist)
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

    return max_total

if __name__=='__main__':
    filename="eighteen.dat"
    cProfile.run('print getmax(filename); print')
