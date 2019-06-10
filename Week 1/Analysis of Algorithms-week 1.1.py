# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 16:43:14 2019

@author: MMOHTASHIM
"""
import time
lists=[x for x in range(-100,10,2)]
##analysis 1 tells how many combinations of three numbers are there where there sum equals to zero(brute_force way)
def analysis_1(lists):
    count=0
    start=time.process_time()
    for i in range(0,len(lists)):
        for j in range(i+1,len(lists)):
            for k in range(j+1,len(lists)):
                if lists[i]+lists[j]+lists[k]==0:
                    count+=1
    end=time.process_time()
    return count,end-start
print(analysis_1(lists))



