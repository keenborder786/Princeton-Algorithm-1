# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:21:59 2019

@author: MMOHTASHIM
"""
import random
def shuffling_sort(arr):
    for i in range(len(arr)):
        r=int(random.uniform(0,len(arr)))
        if r!=i:
            val_1=arr[i]
            arr[i]=arr[r]
            arr[r]=val_1
        else:
            continue
    return arr
print(shuffling_sort([1,3,5,7,84,3]))  