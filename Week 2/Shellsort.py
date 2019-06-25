# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 13:25:44 2019

@author: MMOHTASHIM
"""

def shellshort(arr):
    N=len(arr)
    h=1
    while h<N/3:
        h=(3*h+1)
    while h>=1:
        for i in range(h,N,1):
            for j in range(i,-1,-h):
                if j>0 and j>=h:
                    if arr[j]<arr[j-h]:
                        value_1=arr[j-h]
                        arr[j-h]=arr[j]
                        arr[j]=value_1
                    else:
                        break
                else:
                    break
        h=h//3
    return arr
print(shellshort([1,45,5,312,141,131,33,11,22,-1,1323,33,2,211,232323,100000]))

