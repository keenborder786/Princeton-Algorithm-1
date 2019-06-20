# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:04:45 2019

@author: MMOHTASHIM
"""

def selection_sort(arr):##about quad time(n^2/2)
    N=len(arr)
    for i in range(N):
        mins=i
        for j in range(i+1,N):
            if arr[j]<arr[mins]:
              value_1=arr[i]
              arr[mins]=arr[j]
              arr[j]=value_1
              
    return arr
print(selection_sort([1,4,3,6,45,32,44,666000,234,44,23,4444444,3,222,332,423424234]))
        
    