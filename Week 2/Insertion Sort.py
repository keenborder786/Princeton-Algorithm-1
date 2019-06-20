# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:05:33 2019

@author: MMOHTASHIM
"""

def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i,-1,-1):
            if j>0:
                if arr[j]<arr[j-1]:
                    value_1=arr[j-1]
                    arr[j-1]=arr[j]
                    arr[j]=value_1
                else:
                    break
            else:
                break
    return arr
print(insertion_sort([1,45,5,312,141,131,33,11,22,-1,1323,33,2,211]))