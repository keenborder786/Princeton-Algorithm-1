# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:58:53 2019

@author: MMOHTASHIM
"""
import random
def quick_sort(A):
    quick_sort2(A,0,len(A)-1)

def quick_select(A,low,hi,k):
    if low==hi:
        return A[low]
    split=partition(A,low,hi)
    
    lenght=split-low+1
    if lenght==k:
        return A[split]
    elif k<lenght:
        return quick_select(A,low,split-1,k)
    else:
        return quick_select(A,split+1,hi,k-lenght)
    
    
def quick_sort2(A,low,hi):
    if low<hi:
        p=partition(A,low,hi)
        quick_sort2(A,low,p-1)
        quick_sort2(A,p+1,hi)
    
def partition(A,low,hi):
    pivotIndex=low
    pivotValue=A[pivotIndex]
    border=low
    for i in range(low,hi+1):
        if A[i]<pivotValue:
            border+=1
            A[i],A[border]=A[border],A[i]
    A[low],A[border]=A[border],A[low]
    return border
if __name__=='__main__':
    a=[1231,3121231,3123,33,44,-2,33]
    shuffled = random.sample(a, len(a))
    l=quick_select(a,0,len(a)-1,7)
    print(l)