# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:09:25 2019

@author: MMOHTASHIM
"""
# Iterative Binary Search Function 
# It returns location of x in given array arr if present, 
# else returns -1 
def binarySearch(arr, l, r, x): 
    arr=sorted(arr)
  
    while l <= r: 
  
        mid = round((l + r)/2) 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element was not present 
    return -1
arr = [33,2123,123,3,12,33,44,33,11,44,33,12,122,44,33,1,244,22,34,22,1,55,13,132,44,567,321,3214,32,121,44,121,44444,3013,0,3]
x = 11
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
print(result)




def binary_sum_problem(lists):
    lists=sorted(lists)
    res=[]
    for i in range(len(lists)):
        for a in range(i,len(lists)):
            num_1=lists[i]
            num_2=lists[a]
            if binarySearch(lists, 0, len(lists)-1, -(num_1+num_2))!=-1:
                res.append([num_1,num_2,-(num_1+num_2)])
    return res
            
arr=[30,-40,-20,-10,40,0,10,5]
print(binary_sum_problem(arr))            
            
            

