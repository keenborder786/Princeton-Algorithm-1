# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:44:38 2019

@author: MMOHTASHIM
"""

# Python program for implementation of MergeSort 
def bottom_up_mergesort(list): 
    if len(list) < 2: 
        return list
  
    middle = int(len(list)/2)
    left = mergesort(list[:middle]) 
    right = mergesort(list[middle:]) 
  
    return bottom_up_merge(left, right)
def bottom_up_merge(left, right): 
    if not len(left) or not len(right): 
        return left or right 
  
    result = [] 
    i, j = 0, 0
    while (len(result) < len(left) + len(right)): 
        if left[i] < right[j]: 
            result.append(left[i]) 
            i+= 1
        else: 
            result.append(right[j]) 
            j+= 1
        if i == len(left) or j == len(right): 
            result.extend(left[i:] or right[j:]) 
            break 
  
    return result 
  
print(bottom_up_mergesort([15, 4, 11, 1,231,13123,134,13,-132,3123,44444,3123]))
cut_off=7
def mergesort(arr):##optimized method with cutoff for insertion sort and tweaks for already sorted arrays
    if len(arr)<=1:
        return arr
    midpoint=int(len(arr)/2)
    if midpoint<=cut_off-1:  
        result=insertion_sort(arr)
        return result
    left,right=mergesort(arr[:midpoint]),mergesort(arr[midpoint:])
    if left[-1]<=right[0]:
        result=left.copy()
        result+=right
        return result
    return merge(left,right)


def merge(left,right):
    result=[]
    left_pointer=right_pointer=0
    
    while left_pointer<len(left) and right_pointer<len(right):
        if left[left_pointer]<right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer+=1
        else:
            result.append(right[right_pointer])
            right_pointer+=1
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    
    return result
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

def main():
    arr=[11,5,15,16]
    print(arr)
    result=mergesort(arr)
    print(result)
    
if __name__=='__main__':
    main()