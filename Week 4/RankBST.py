# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 17:47:45 2019

@author: MMOHTASHIM
"""

# Python3 program to find rank of an  
# element in a stream.  
  
class newNode: 
    def __init__(self, data): 
        self.data = data  
        self.left = self.right = None
        self.leftSize = 0
  
# Inserting a new Node.  
def insert(root, data): 
    if root == None:  
        return newNode(data)   
  
    # Updating size of left subtree.  
    if data <= root.data:  
        root.left = insert(root.left, data)  
        root.leftSize += 1
    else: 
        root.right = insert(root.right, data) 
    return root 
  
# Function to get Rank of a Node x.  
def getRank(root, x): 
      
    # Step 1.  
    if root.data == x: 
        return root.leftSize  
  
    # Step 2.  
    if x < root.data:  
        if root.left == None:  
            return -1
        else: 
            return getRank(root.left, x) 
  
    # Step 3.  
    else:  
        if root.right == None:  
            return -1
        else:  
            rightSize = getRank(root.right, x)  
            return root.leftSize + 1 + rightSize 
  
# Driver code  
if __name__ == '__main__': 
    arr = [5, 1, 4, 4, 5, 9, 7, 13, 3]  
    n = len(arr)  
    x = 4
  
    root = None
    for i in range(n): 
        root = insert(root, arr[i]) 
  
    print("Rank of", x, "in stream is:",  
                       getRank(root, x)) 
    x = 13
    print("Rank of", x, "in stream is:",  
                       getRank(root, x)) 
  
# This code is contributed by PranchalK