# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:49:02 2019

@author: MMOHTASHIM
"""
##min-oriented
class MinBinHeap(object):
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    def Heapshort(self):
        sorteds=[]
        while (self.currentSize>0):
#            print(self.delMin())
            print(self.currentSize)
            sorteds.append(self.delMin())
        return sorteds
    
    
    
    
    
    
    
    
    
    
    
    
class MaxBinHeap(object):
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[i//2]
                self.heapList[i//2] = tmp
            i = i // 2

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                tmp = self.heapList[mc]
                self.heapList[mc] = self.heapList[i]
                self.heapList[i] = tmp
            i = mc
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
    def maxChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2+1
            else:
                return i * 2 
    def Heapshort(self):
        sorteds=[]
        while (self.currentSize>0):
#            print(self.delMin())
            print(self.currentSize)
            sorteds.append(self.delMax())
        return sorteds
    def delMax(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval  


if __name__=="__main__":
    heap_min=MinBinHeap()
    heap_min.buildHeap([33,44,1,3,4,6,8,9])
    print(heap_min.currentSize)
    print(heap_min.heapList)
    print(heap_min.Heapshort())
    
    
    heap_max=MaxBinHeap()
    heap_max.buildHeap([33,44,1,3,4,6,8,9])
    print(heap_max.currentSize)
    print(heap_max.heapList)
    print(heap_max.Heapshort())
    
    