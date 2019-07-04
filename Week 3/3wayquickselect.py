# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:34:32 2019

@author: gist//User:adonese
"""
import random
def partition3(A, l, r):
    lt = l  # We initiate lt to be the part that is less than the pivot
    i = l   # We scan the array from left to right
    gt = r  # The part that is greater than the pivot
    pivot = A[l]    # The pivot, chosen to be the first element of the array, that why we'll randomize the first elements position
                    # in the quick_sort function.
    while i <= gt:      # Starting from the first element.
        if A[i] < pivot:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > pivot:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1
            
    return lt, gt



def quick_sort(A, l, r):
    """
    quick_sort: One of the most used sorting algorithm. 
    It makes to recursive calls. One to sort the left part separately, other for sorting the right part.
    The partition key is chosen randomly via ``random.randint(l, r)`` and it's between the ``l,  r``.
    
    PARAMETERS:
    -----------
    A: Array or the sequence that we want to sort.
    l: The lower bound of the array that we want to sort. It's not very important we might replace it by a wrapper function
    that only takes in an array as input. In this case it's the first element in the left part of the array.
    r: It's the same as l, only differs as it's the first element from the end.
    
    RETURNS:
    -------
    Sorted list A.
    """
    if l >= r: 
        return
    k = random.randint(l, r)
    A[k], A[l] = A[l], A[k]
    
    lt, gt = partition3(A, l, r)
    quick_sort(A, l, lt - 1)
    quick_sort(A, gt + 1, r)


if __name__=='__main__':
    a=[1231,3121231,3123,33,44,-2,33]
    shuffled = random.sample(a, len(a))
    l=quick_sort(a,0,len(a)-1)
    print(a)


