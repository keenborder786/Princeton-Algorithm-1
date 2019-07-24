# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:59:52 2019

@author: MMOHTASHIM
"""

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
        self.size=0
# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                    
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')
def ceil(root, inp):     
    # Base Case 
        if root == None: 
            return -1
      
    # We found equal key 
        if root.data == inp : 
            return root.data  
      
    # If root's key is smaller, ceil must be in right subtree 
        if root.data < inp: 
            return ceil(root.right, inp) 
      
    # Else, either left subtre or root has the ceil value 
        val = ceil(root.left, inp) 
        return val if val >= inp else root.data  


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
