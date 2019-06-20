# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:28:05 2019

@author: MMOHTASHIM
"""
from numpy.random import choice
import numpy as np
class Dequeue(object):
    def __init__(self):
        self.arr=[]
        self.size=0
    def isempty(self):
        return self.size==0
    def get_sizes(self):
        return self.size
    def addFirst(self,var):
        self.arr.insert(0,var)
        self.size+=1
    def addLast(self,var):
        self.arr.append(var)
        self.size+=1
    def removeFirst(self):
        del self.arr[0]
        self.size-=1
    def removeLast(self):
        self.arr.pop()
        self.size-=1
    def iterator(self):
        for i in self.arr:
            print(i)

class Randomizedqueue(object):
    def __init__(self):
        self.arr=[]
        self.size=0
    def isempty(self):
        return self.size==0
    def get_sizes(self):
        return self.size
    def enqueue(self,var):
        self.arr.insert(0,var)
        self.size+=1
    def sample(self):
        return choice(self.arr)
    def dequeue(self):
        item=self.sample()
        index=self.arr.index(item)
        del self.arr[index]
        self.size-=1
    def iterator(self):
        for i in self.arr:
            print(i)

def permutation(k,stri):
    unique=[]
    for i in stri:
        if i not in unique:
            unique.append(i)
    ks_unique=[]
    i=0
    while i<k:
        item=choice(unique)
        if item not in ks_unique:
            ks_unique.append(item)
            i+=1
            print(item)
permutation(3,["d","a","D","l","How","Yes","A"])








        
        
    
        